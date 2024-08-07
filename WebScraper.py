import requests as rq
from bs4 import BeautifulSoup as bs


def getRawWebSiteHTML(link):
    req = rq.get(link)
    return bs(req.content)

def getTablesFromWebPage(link):
    webPage = getRawWebSiteHTML(link)
    return webPage.find_all('table')

def getStrengthTable(link):
    allTables = getTablesFromWebPage(link)
    strengthTable = allTables[2]
    resultList = []
    for rows in strengthTable.find_all('tr'):
        newList = []
        for item in rows.find_all('td'):
            #print(item.text)
            newList.append(int(item.text))
        if len(newList) > 0:
            resultList.append(newList)

    return resultList


strengthTable = getStrengthTable("https://strengthlevel.com/strength-standards/bench-press")
print(strengthTable)
