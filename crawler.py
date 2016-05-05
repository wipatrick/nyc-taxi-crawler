import requests, wget
from bs4 import BeautifulSoup

url = "http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml"
r = requests.get(url)
soup = BeautifulSoup(r.content)

links = soup.find_all("a")

for link in links:
    if link.text == "Yellow":
        file = link.get("href")
        wget.download(file)
