
# pip install beautifulsoup4
# pip install lxml
# pip install html5lib
# pip install requests



from bs4 import BeautifulSoup
import requests
# url = "https://www.tutorialspoint.com"
# url = "https://www.http://www.monstertower.com"
url = "https://www.instructables.com/Ten-Breadboard-Projects-For-Beginners/"
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
print(soup.title)

for link in soup.find_all('a'):
    print(link.get('href'))




