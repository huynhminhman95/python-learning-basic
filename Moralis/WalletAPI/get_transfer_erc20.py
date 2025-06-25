"""
Get ERC20 token transfer by wallet: lay danh sach chuyen giao token ERC20 theo dia chi vi
"""

import json
from moralis_config import get_moralis_api, get_api_key, get_transaction_params

# Get API instance and key
evm_api = get_moralis_api()
api_key = get_api_key()

# Get parameters for transaction API call
params = get_transaction_params(
   address="0x1234567890abcdef1234567890abcdef12345678",
   chain="eth",
   limit=5
)

response = evm_api.token.get_wallet_token_transfers(
   api_key=api_key,
   params=params
)

# In kết quả dưới dạng JSON đẹp
print(json.dumps(response, indent=2, ensure_ascii=False))