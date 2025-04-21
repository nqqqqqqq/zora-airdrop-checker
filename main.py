import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

# Читаем кошельки из файла
with open("wallets.txt", "r") as f:
    wallets = [line.strip() for line in f if line.strip()]

url = "https://api.zora.co/universal/graphql"

headers = {
    "accept": "application/json, multipart/mixed",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "origin": "https://api.zora.co",
    "referer": "https://api.zora.co/universal/graphql",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
}

query_template = """
query {{
  zoraTokenAllocation(
    identifierWalletAddresses: ["{wallet}"],
    zoraClaimContractEnv: PRODUCTION
  ) {{
    totalTokensEarned {{
      totalTokens
    }}
  }}
}}
"""

lock = Lock()

def process_wallet(wallet):
    query = query_template.format(wallet=wallet)
    payload = {"query": query}
    while True:
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            tokens = data["data"]["zoraTokenAllocation"]["totalTokensEarned"]["totalTokens"]

            if tokens > 0:
                result_line = f"{wallet}:{tokens}\n"
                with lock:
                    with open("good.txt", "a") as good_file:
                        good_file.write(result_line)
                print(result_line.strip())
            break
        except Exception as e:
            print(f"{wallet}: ошибка или нет ответа, пробуем снова... ({e})")
            time.sleep(1)

with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(process_wallet, wallets)