import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
from moralis_config import get_moralis_api, get_api_key, get_wallet_history_params

# Get API instance and key
evm_api = get_moralis_api()
api_key = get_api_key()

# Get parameters for wallet history API call
params = get_wallet_history_params(
   chain="eth",
   address="0x1f9090aaE28b8a3dCeaDf281B0F12828e676c326"
)

result = evm_api.token.get_wallet_token_balances(
    api_key=api_key,
    params=params,
)

# Display result in JSON format
print(json.dumps(result, indent=2, ensure_ascii=False))