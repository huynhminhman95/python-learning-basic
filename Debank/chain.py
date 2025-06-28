import os
from dotenv import load_dotenv
import requests
import time

load_dotenv()
api_key = os.getenv("DEBANK_API_KEY")

# Debug: Kiểm tra API key
if not api_key:
    print("❌ DEBANK_API_KEY not found in .env file!")
    print("Please add: DEBANK_API_KEY=your_api_key_here")
    exit(1)
else:
    print(f"🔑 API Key loaded: {api_key[:10]}...")

url = "https://pro-openapi.debank.com/v1/chain/list"
headers = {
    "accept": "application/json",
    "AccessKey": api_key
}

def fetch_data():
    try:
        # Thêm delay trước khi gọi API
        time.sleep(1)
        
        print(f"🌐 Calling: {url}")
        print(f"🔑 Using API key: {api_key[:10] if api_key else 'None'}...")
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print("✅ Success!")
            print("Response JSON:", response.json())
        elif response.status_code == 403:
            print("❌ Quota exceeded or forbidden. Please check API key and rate limits.")
            print("Response:", response.text)
        elif response.status_code == 401:
            print("❌ Unauthorized. Please check your API key.")
            print("Response:", response.text)
            print("💡 Make sure your API key is valid and has the correct permissions.")
        elif response.status_code == 429:
            print("❌ Rate limit exceeded. Please wait and try again.")
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
            
    except Exception as e:
        print("❌ Error:", e)

fetch_data()
