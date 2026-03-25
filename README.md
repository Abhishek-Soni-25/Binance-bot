# 🚀 Binance Futures CLI Trading Bot

A simple, production-style Python CLI application to place **MARKET** and **LIMIT** orders on Binance Futures Testnet.

This project demonstrates clean backend design, API integration, structured logging, and robust error handling — similar to real-world trading systems.

---

## 📌 Overview

This bot allows users to place trades on Binance Futures Testnet using command-line inputs.

It is designed with:
- Modular architecture
- Clear separation of concerns
- Clean logging (useful, not noisy)
- Input validation and error handling

---

## 🌟 Features

- 📈 **Market Orders**
  - Instant execution at current market price

- 🎯 **Limit Orders**
  - Execute trades at user-defined price

- 🔄 **BUY & SELL Support**
  - Supports both long and short operations

- 🧠 **Input Validation**
  - Validates symbol, order type, quantity, and price

- 📝 **Structured Logging**
  - Logs only important events (intent, success, failure)

- ⚠️ **Error Handling**
  - Handles API errors, invalid inputs, and network issues

---

## 🏗️ Project Structure

```
binance-futures-cli-bot/
│
├── bot/
│   ├── client.py        # Binance API client setup
│   ├── orders.py        # Order execution logic
│   ├── validators.py    # Input validation
│   ├── logger.py        # Logging configuration
│
├── main.py              # CLI entry point
├── config.py            # Environment configuration
├── requirements.txt
├── logs/
│   └── trading.log      # Log file
└── .env                 # API credentials (not committed)
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Abhishek-Soni-25/Binance-bot.git
cd Binance-bot
```

---

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

---

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

### 4. Configure API credentials

Create a `.env` file in the root directory:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_SECRET_KEY=your_testnet_secret_key
BASE_URL=https://testnet.binancefuture.com
```

---

## 🚀 Usage

### ✅ Place a Market Order
```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.01
```

---

### ✅ Place a Limit Order
```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.01 --price 72000
```

---

## 📊 CLI Parameters

| Parameter | Description |
|----------|------------|
| `--symbol` | Trading pair (e.g., BTCUSDT) |
| `--side` | BUY or SELL |
| `--type` | MARKET or LIMIT |
| `--qty` | Quantity to trade |
| `--price` | Required for LIMIT orders |

---

## 🧾 Example Output

```
Order Summary:
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.01

Order Placed Successfully!
Order ID: 12991663890
Status: FILLED
Executed Qty: 0.01
Avg Price: 71261.3
```

---

## 📝 Logging

Logs are stored in:
```
logs/trading.log
```

### Example Logs

```
INFO  - Placing MARKET order | Symbol=BTCUSDT | Side=BUY | Qty=0.01
INFO  - Order SUCCESS | ID=12991663890 | Status=FILLED | ExecutedQty=0.01 | AvgPrice=71261.3
ERROR - Order FAILED | Symbol=BTCUSDT | Side=SELL | Reason=Timestamp ahead of server time
```