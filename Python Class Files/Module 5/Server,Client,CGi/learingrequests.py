import requests
from bs4 import BeautifulSoup

url = 'https://www.github.com/jadhavsharad'
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

title = soup.find("title").text
print('Title :',title)

