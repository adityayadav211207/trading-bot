# 🤖 Binance Futures Trading Bot

A simple but effective Python bot to place market and limit orders on Binance Futures using the official Binance API.

---

## 📦 Features

- ✅ Supports **MARKET** and **LIMIT** order types  
- ✅ Works with **Binance Futures Testnet** by default  
- ✅ Built-in **error handling** and **logging**  
- ✅ **Environment variable support** for secure API key management  
- ✅ Clean shutdown with `Ctrl + C`  

---

## ⚙️ Requirements

- Python 3.7+
- Binance API keys
- pip packages:

```bash
pip install python-binance

🔐 Secure Setup (No API Keys in Code)
This bot does not store your Binance API credentials in the source code.


🚀 How to Run
1. Clone the Repository

git clone https://github.com/yourusername/binance-trading-bot.git
cd binance-trading-bot
2. Install Dependencies

pip install -r requirements.txt
If requirements.txt doesn't exist, just run:


pip install python-binance
3. Set Your API Credentials
🔹 On Linux/macOS

export BINANCE_API_KEY='your_api_key_here'
export BINANCE_API_SECRET='your_api_secret_here'
🔹 On Windows (Command Prompt)

set BINANCE_API_KEY=your_api_key_here
set BINANCE_API_SECRET=your_api_secret_here
4. Run the Bot

python trading_bot.py
You will be prompted to enter:

Trading pair (e.g., BTCUSDT)

Side (BUY or SELL)

Order type (MARKET or LIMIT)

Quantity

Price (for LIMIT orders)

📝 Example Session

Enter trading pair (e.g., BTCUSDT): BTCUSDT
Enter order side (BUY/SELL): BUY
Enter order type (MARKET/LIMIT): MARKET
Enter quantity: 0.001
🧯 Safety Notes
This bot defaults to testnet mode. You can modify the code to switch to live trading (at your own risk).

Always double-check your inputs and test with small amounts.

For production use, consider rate limit handling, retry logic, and order book monitoring.

📁 Logging
All activity is logged in trading_bot.log:

tail -f trading_bot.log
🛠️ Customization Ideas
Add Take-Profit / Stop-Loss support

Integrate with a trading strategy or signal provider

Use .env file with python-dotenv for smoother setup

📜 License
MIT License © 2025 YourNameHere

💬 Questions or Issues?
Open an issue or email you@example.com.

Happy Trading! 📈


---

Would you like this `README.md` bundled with a sample `.env` file and `requirements.txt` for distribution? I can generate those too.
