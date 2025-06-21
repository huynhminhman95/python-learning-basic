import os
from dotenv import load_dotenv

load_dotenv()

MORALIS_API_KEY = os.getenv("MORALIS_API_KEY")

# Validate API key
if MORALIS_API_KEY is None:
    print("Warning: MORALIS_API_KEY environment variable is not set!")
    print("Please create a .env file in the root directory with:")
    print("MORALIS_API_KEY=your_api_key_here")
else:
    print(f"API Key loaded: {MORALIS_API_KEY[:10]}...")