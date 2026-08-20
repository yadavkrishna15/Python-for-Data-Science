import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Rohit_Sharma"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/151.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    print("=" * 60)
    print("WIKIPEDIA ROHIT SHARMA PAGE WEB SCRAPING")
    print("=" * 60)

    # Rest of your code remains the same...
