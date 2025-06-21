import json
from moralis_config import get_moralis_api, get_api_key, get_transaction_params

# Get API instance and key
evm_api = get_moralis_api()
api_key = get_api_key()

# Get parameters for transaction API call
params = get_transaction_params(
    address="0x1234567890abcdef1234567890abcdef12345678",  # Địa chỉ ví
    chain="eth",          # Hoặc 'polygon', 'bsc', 'avalanche',...
    limit=10              # Lấy 10 giao dịch gần nhất
)

response = evm_api.transaction.get_wallet_transactions(
    api_key=api_key,
    params=params
)

# In ra danh sách giao dịch
for tx in response["result"]:
    print(f"Hash: {tx['hash']}")
    print(f"From: {tx['from_address']}")
    print(f"To: {tx['to_address']}")
    print(f"Value (Wei):  {tx['value']}")
    print(f"Gas used: {tx['receipt_gas_used']}")
    print(f"Block: {tx['block_number']}")
    print(f"--------------------------")
