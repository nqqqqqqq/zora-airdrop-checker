# 🪂 Zora Airdrop Checker

A script for checking the amount of tokens received by wallets in the Zora airdrop. Supports multithreading for fast processing of large wallet lists.

## 📦 Features

- Reads wallet addresses from `wallets.txt`
- Sends GraphQL queries to [Zora API](https://api.zora.co/universal/graphql)
- Retries on errors or server overload
- Saves wallets with non-zero token balances to `good.txt`
- Multithreaded wallet processing

## 🚀 Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/zora-airdrop-checker.git
   cd zora-airdrop-checker
   ```

2. Install dependencies (activate a virtual environment if you're using one):
   ```bash
   pip install -r requirements.txt
   ```

3. Add wallet addresses to `wallets.txt` — one per line:
   ```
   0x3cbaabc6789379ecd806fa356c791c7b94931868
   0x1234567890abcdef1234567890abcdef12345678
   ...
   ```

4. Run the script:
   ```bash
   python main.py
   ```

5. Results will be saved to `good.txt` in the format:
   ```
   0xabc123...:115.48672
   ```

## 🛠 Configuration

- You can change the number of threads by modifying `max_workers` in `main.py`:
  ```python
  with ThreadPoolExecutor(max_workers=10) as executor:
  ```

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
