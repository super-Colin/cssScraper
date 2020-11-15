
from bs4 import BeautifulSoup
import requests


def scrapeSite(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    print(soup.title)
    print(soup.a['href)



with open('index.html', 'r') as f:
    content = f.read()
    soup = BeautifulSoup(content, 'lxml')
    print(soup.a['href'])
    scrapeSite(soup.a['href'])







