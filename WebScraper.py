import requests as rq


def getWebSiteData(link):
    req = rq.get(link)
    print(req.content)
    return req

getWebSiteData("https://geislerc.github.io/")
