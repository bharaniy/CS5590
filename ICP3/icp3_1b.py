import requests
url=requests.get("https://en.wikipedia.org/wiki/Deep_learning").text
from bs4 import BeautifulSoup
soup: BeautifulSoup=BeautifulSoup(url,'html.parser')
print("\nTitle of web page:",soup.title.string)
print(soup.find_all('a'))
for link in soup.find_all('a'):
    print(link.get('href'))