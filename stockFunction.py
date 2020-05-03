import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def getPrice(url):
    myURL = url
    uClient = uReq(myURL)
    pageHTML = uClient.read()
    pageSoup = soup(pageHTML, "html.parser")
    spans = pageSoup.find_all("span")
    price = spans[13].string
    price = price.replace(",", ".")
    return float(price)

