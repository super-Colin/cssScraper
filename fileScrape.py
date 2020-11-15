
from bs4 import BeautifulSoup
# import requests as reqs



with open('index.html', 'r') as f:
    content = f.read()
    soup = BeautifulSoup(content, 'lxml')
    classesUsed = list()

    for tag in soup.body.find_all():
        if tag.has_attr('class'):
            classesUsed.append(tag['class'])







