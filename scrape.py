
import requests
import re  # regex for later, native to python
from bs4 import BeautifulSoup

from tinydb import TinyDB, Query  # "pip install -U tinydb"

domainUrlString = 'supercolin.dev'
scrapeDBString = './' + domainUrlString + '.json'
completeUrlString = 'https://www.' + domainUrlString

open( scrapeDBString, 'w')

scrapeDB = TinyDB(scrapeDBString)



def makeSoup(url):
    resp = requests.get(url)
    return BeautifulSoup(resp.text, 'lxml')


def grabTagUrlCallback(tag):
    if tag.has_attr('href'):
        return tag['href']
    return False

def grabTagClassCallback(tag):
    if tag.has_attr('class'):
        return tag['class']
    return False






# def addToDBWithoutDuplicates(): # Expects list
#     scrapeDB.insert({"urls":'urls'})




def parseSoupWithCallbacks( beautifulSoup, dictionaryOfCallbacks = {}):
    parseResults = {}
    for callbackTitle in dictionaryOfCallbacks:
        parseResults[callbackTitle] = []

    for tag in beautifulSoup.body.find_all(): # for every tag in the soup
        for callbackTitle in dictionaryOfCallbacks: # for every callback funtion, check every function on tag

            callbackResult = dictionaryOfCallbacks[callbackTitle](tag)
            if callbackResult:
                parseResults[callbackTitle].append(callbackResult)
                
            # print(callbackTitle)
            # print(dictionaryOfCallbacks[callbackTitle])

    print(parseResults)



parseSoupWithCallbacks(makeSoup(completeUrlString), {'urls':grabTagUrlCallback, 'classes':grabTagClassCallback}, )




# def scrapeSoupForUrls(soup):  # expects BeautifulSoup
#     pageUrls = []
#     for link in soup.body.find_all('a'):
#         pageUrls.append(link.get('href'))
#     return pageUrls  # returns a list




