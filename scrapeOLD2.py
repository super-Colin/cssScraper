
# pip install beautifulsoup4
# pip install lxml
# pip install html5lib
# pip install requests

from bs4 import BeautifulSoup

with open('index.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')

    # print(soup.h2)
    # print(soup.head)
    # print(soup.li)

    # for child in soup.recursiveChildGenerator():
    #     if child.name:
    #         print(child.name)

    # root = soup.html
    # rootChildren = [e.name for e in root.children]
    # print(rootChildren)

    root = soup.body
    rootChildren = [e.name for e in soup.descendants if e.name is not None]
    print(rootChildren)
    
# https://www.ecosia.org/search?q=potatoes
