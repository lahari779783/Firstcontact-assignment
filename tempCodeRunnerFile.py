import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables from .env file
load_dotenv()

# Securely get the API key from environment variable
API_KEY = os.getenv("GATHER_API_KEY")

# IMPORTANT: Backslash (\) is needed between ID and space name
SPACE_ID = "1WWSGGrEs4MrBXxw\\assignment"

# Email guestlist object
GUESTLIST = {
    "contact.firstcontact@gmail.com": {
        "name": "First Contact",
        "affiliation": "Test",
        "role": ""
    }
}

# API endpoint
url = "https://api.gather.town/api/setEmailGuestlist"

# Payload
payload = {
    "apiKey": API_KEY,
    "spaceId": SPACE_ID,
    "guestlist": GUESTLIST,
    "overwrite": True
}

# Send POST request
response = requests.post(
    url,
    headers={"Content-Type": "application/json"},
    data=json.dumps(payload)
)

# Check result
if response.status_code == 200:
    print("✅ Guest list successfully updated!")
else:
    print("❌ Failed to update guest list.")
    print("Status code:", response.status_code)
    print("Response:", response.text)
