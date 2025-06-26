import os
import sys
from dotenv import load_dotenv
from typing import Any

# Load environment variables
load_dotenv()

# Add the parent directory to the Python path to import the main config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

try:
    from config import MORALIS_API_KEY
except ImportError:
    print("Error: Could not import main config.py")
    print("Make sure config.py exists in the root directory of the project")
    sys.exit(1)

# Check if API key is available
if MORALIS_API_KEY is None:
    print("Error: MORALIS_API_KEY environment variable is not set!")
    print("Please set your Moralis API key in the .env file")
    sys.exit(1)

# Import Moralis API
from moralis import evm_api

# Global configuration
MORALIS_CONFIG = {
    "api_key": MORALIS_API_KEY,
    "default_chain": "eth",
    "default_limit": 10
}

# Common parameters for different API calls
def get_wallet_history_params(address: str, chain: str = "eth", order: str = "DESC") -> Any:
    """Get parameters for wallet history API call"""
    return {
        "chain": chain,
        "order": order,
        "address": address
    }

def get_balances_params(chain: str = "eth") -> Any:
    """Get parameters for wallet history API call"""
    return {
        "chain": chain
    }

def get_transaction_params(address: str, chain: str = "eth", limit: int = 10) -> Any:
    """Get parameters for transaction API call"""
    return {
        "address": address,
        "chain": chain,
        "limit": limit
    }

# Helper functions
def get_moralis_api():
    """Get the Moralis EVM API instance"""
    return evm_api

def get_api_key():
    """Get the Moralis API key"""
    return MORALIS_API_KEY 