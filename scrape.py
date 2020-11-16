
import requests
import re  # regex for later, native to python
from bs4 import BeautifulSoup

from tinydb import TinyDB, Query  # "pip install -U tinydb"

domainUrlString = 'supercolin.dev'
scrapeDBString = './' + domainUrlString + '.json'
completeUrlString = 'https://' + domainUrlString

open( scrapeDBString, 'w')

scrapeDB = TinyDB(scrapeDBString)



def makeSoup(formattedUrl):
    resp = requests.get(formattedUrl)
    return BeautifulSoup(resp.text, 'lxml')


def grabTagUrlCallback(tag):
    if tag.has_attr('href'):
        return tag['href']
    return False

def grabTagClassesCallback(tag):
    if tag.has_attr('class'):
        return tag['class']
    return False

def grabTagIdsCallback(tag):
    if tag.has_attr('id'):
        return tag['id']
    return False



def findItemsNewToList(referenceList, listToFindNew): # returns items that appear in listToFindNew but not in referenceList
    formattedListToFindNew = []
    for item in listToFindNew:
        if type(item) == list:
            formattedListToFindNew += item
        else:
            formattedListToFindNew.append(item)
    mainListSet = set(referenceList)
    newItemsListSet = set(formattedListToFindNew)
    listOfNewItemsToAdd = list(newItemsListSet - mainListSet)
    return listOfNewItemsToAdd

def combineLists(referenceList, listToAdd):
    return referenceList + findItemsNewToList(referenceList, listToAdd)



def initScrapeDbCategories(callbacksDictionary):
    for title in callbacksDictionary:
        if not scrapeDB.search(Query().type == title):
            scrapeDB.insert({'type' : title, title : []})


def updateDbCategory(categoryTitle, categoryResultsList):
    oldCategoryInfo = scrapeDB.search(Query().type == categoryTitle)[0][categoryTitle]
    updatedCategoryInfo = combineLists(oldCategoryInfo, categoryResultsList)
    scrapeDB.update({categoryTitle : updatedCategoryInfo}, Query().type == categoryTitle)





def parseSoupAllTagsWithCallbacks( beautifulSoup, dictionaryOfCallbacks = {}):
    parseResults = {}
    for callbackTitle in dictionaryOfCallbacks:
        parseResults[callbackTitle] = []

    for tag in beautifulSoup.body.find_all(): # for every tag in the soup
        for callbackTitle in dictionaryOfCallbacks: # for every callback funtion, check every function on tag

            callbackResult = dictionaryOfCallbacks[callbackTitle](tag)
            if callbackResult:
                parseResults[callbackTitle].append(callbackResult)

    return parseResults # returns the results in a dictionary with results with the same callBackTitle



def runCallbacksOnPageUpdateDb(formattedUrl, callbacksDictionary):
    initScrapeDbCategories(callbacksDictionary)
    soup = makeSoup(formattedUrl)
    parseResults = parseSoupAllTagsWithCallbacks(soup, callbacksDictionary)
    for item in parseResults:
        updateDbCategory(item, parseResults[item])


def loopThroughPagesAllTags(listOfFormattedPageUrls, callbacksDictionary):
    pagesCategory = 'pagesVisited'
    initScrapeDbCategories(pagesCategory)
    for pageLink in listOfFormattedPageUrls:
        runCallbacksOnPageUpdateDb(pageLink, callbacksDictionary)
        pastVisited = scrapeDB.search(Query().type == pagesCategory)
        allVisited = pastVisited.append(pageLink)
        scrapeDB.update({pagesCategory: allVisited}, Query().type == pagesCategory)



# runCallbacksOnPageUpdateDb(completeUrlString,  {
#     # 'urls': grabTagUrlCallback,
#     'ids': grabTagIdsCallback,
#     'classes': grabTagClassesCallback
# })

loopThroughPagesList = [
    'https://supercolin.dev/open-circuit-and-short-circuit/',
    'https://supercolin.dev/thevenin-equivalent-and-norton-equivalent-circuits/'
]
loopThroughPagesAllTags(loopThroughPagesList,  {
    'ids': grabTagIdsCallback,
    'classes': grabTagClassesCallback
})




