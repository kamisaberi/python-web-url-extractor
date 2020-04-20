import requests
from bs4 import BeautifulSoup


def recursiveUrl(url, link, depth):
    if depth == 5:
        return url
    else:
        print(link['href'])
        page = requests.get(url + link['href'])
        soup = BeautifulSoup(page.text, 'html.parser')
        newlink = soup.find('a')
        if len(newlink) == 0:
            return link
        else:
            return link, recursiveUrl(url, newlink, depth + 1)


def getLinks(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        links.append(recursiveUrl(url, link, 0))
    return links


links = getLinks("https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html")
print(links)
