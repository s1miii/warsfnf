## Requirements
- VPS with Python 3.10+
- ETH on Base chain in your wallet

## Setup

### 1. Install dependencies
```bash
pip install web3 httpx eth-account --break-system-packages
```

### 2. Upload `bean_bot.py` to your VPS
Upload the file to any folder, for example `/root/bean_bot.py`

### 3. Edit your config
Open the file and edit ONLY the top section:
```bash
nano bean_bot.py
```
Change these settings:
```
PRIVATE_KEY = "0xYOUR_PRIVATE_KEY_HERE"   <-- REQUIRED: your wallet private key
NUM_BLOCKS = 5                             <-- blocks per round (1-25)
ETH_PER_ROUND = 0.002                     <-- ETH to bet each round
MIN_EV = 0.0                              <-- minimum EV to play (0 = breakeven)
WAIT_SECONDS = 35                          <-- wait before double-checking EV
AUTO_CLAIM = True                          <-- auto claim rewards (True/False)
CLAIM_ETH_MIN = 0.01                       <-- claim ETH when above this amount
CLAIM_BEAN_MIN = 0.1                       <-- claim BEAN when above this amount
CLAIM_CHECK_INTERVAL = 30                  <-- check rewards every X seconds
```
Save: `Ctrl+O` then `Enter` then `Ctrl+X`

**DO NOT edit anything below the config section.**

### 4. Run the bot
```bash
python3 bean_bot.py
```

## Run 24/7 (keep running after you close terminal)

### Option A: Screen
```bash
screen -S bean
python3 bean_bot.py
```
Detach: `Ctrl+A` then `D`
Reattach: `screen -r bean`
