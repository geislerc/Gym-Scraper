import requests as rq
from bs4 import BeautifulSoup as bs


def getRawWebSiteHTML(link):
    req = rq.get(link)
    return req


htmlStuff = getRawWebSiteHTML("https://geislerc.github.io/")
soup = bs(htmlStuff.content)
print(soup.prettify())
