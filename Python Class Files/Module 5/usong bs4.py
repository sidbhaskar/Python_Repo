import requests
from bs4 import BeautifulSoup

url = 'https://www.apple.com/'
response = requests.get(url)

if response.status_code == 200 :
    html_content = response.text
    css_content = response.text
print(html_content)
print('-------------------------------------------------------------------------------')
