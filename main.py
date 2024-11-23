import requests
import json

API_KEY = "75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6"
BASE_URL = "https://api.meraki.com/api/v1"

def get_organizations():
    headers = {
        "Content-Type": "application/json",
        "X-Cisco-Meraki-API-Key": API_KEY
    }
    response = requests.get(f"{BASE_URL}/organizations", headers=headers)
    response.raise_for_status()  # Validación de errores
    return response.json()

if __name__ == "__main__":
    organizations = get_organizations()
    print(json.dumps(organizations, indent=4))