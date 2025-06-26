"""
Get decoded transactions by wallet: Lay danh sach cac giao dich da giai ma theo dia chi vi
Use: dia chi vi goi func gi, giao dich token,mint nft, gui token erc20..., xem ro cac input/output
"""

import sys
import os
from turtle import clear
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

import json
from Moralis.WalletAPI.moralis_config import get_moralis_api, get_api_key, get_transaction_params

# Get API instance and key
evm_api = get_moralis_api()
api_key = get_api_key()

# Get parameters for transaction API call
params = get_transaction_params(
   address="0x1234567890abcdef1234567890abcdef12345678",
   chain="eth",
   limit=5
)

response = evm_api.transaction.get_wallet_transactions_verbose(
   api_key=api_key,
   params=params
)

# print(response)
for tx in response["result"]:
    print(f"Hash: {tx['hash']}")
    print(f"From: {tx['from_address']}")
    print(f"To: {tx['to_address']}")
    print(f"Value (Wei):  {tx['value']}")
    print(f"Gas used: {tx['receipt_gas_used']}")
    print(f"Block: {tx['block_number']}")
    print(f"--------------------------")