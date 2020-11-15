
from bs4 import BeautifulSoup
# import requests as reqs


def hasClass(element):
    # print(element.has_attr('class'))
    # print(element)
    return element.has_attr('class') and not element.has_attr('id')


with open('index.html', 'r') as f:
    content = f.read()
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.select_one('.myClass'))
    # print(soup.find_all(hasClass))
    nestedContainers = soup.select('.container .container')
    print(nestedContainers)





# print(soup.title)
# print(soup.title.text)
# print(soup.title.parent)

# print(soup.prettify())





