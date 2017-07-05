import urllib3
from bs4 import BeautifulSoup

NAT_GEO_PICOFTHEDAY = "http://www.nationalgeographic.com/photography/photo-of-the-day/"

http = urllib3.PoolManager()
response = http.request("GET", NAT_GEO_PICOFTHEDAY)

if response.status != 200:
    exit(1)

soup = BeautifulSoup(response.data, "html.parser")
content = soup.find("meta", {"name": "twitter:image:src"})['content']
print(content)
