import requests
import lxml.html
import lxml.etree


class Url:
    def __init__(self, url):
        self._url = url
        self._descendants = set()
        self._descendant_counter = 0


def britishCrawler(url, verifyXpath, descendantXpaths, ancestorXpaths, royaltyXpaths):
    urls = []
    start_url = Url(url)
    max_urls = 30
    urls_counter = 0
    # start crawling
    while True:
        # exit
        if urls_counter == max_urls:
            break
        # check if it is royalty member.
        # get urls according to type.




    return urls


if __name__ == '__main__':
    url = ""
    verifyXpath = "//table[@class = 'infobox vcard']//a[contains(@title, 'of the United Kingdom')]/@href[contains(., 'wiki')] | " \
                  "//div[@class='plainlist']//a//text()[contains(.,'Windsor')]/..//@href[contains(.,'/wiki/')]"
    descendantXpaths = "//table[@class = 'infobox vcard']/tbody/tr/th[contains(text(),'Issue')]/..//a""/@href[contains(., 'wiki')]"
    ancestorXpaths = ""
    royaltyXpaths = ["//table[@class = 'infobox vcard']/tbody/tr/th[contains(text(),'Predecessor')]/..//a/@href[contains(., 'wiki')]",
                     "//table[@class = 'infobox vcard']/tbody/tr/th[contains(text(),'Successor')]/..//a/@href[contains(., 'wiki')]",
                     "//td[@class = 'sidebar-content']"]

    urls = britishCrawler(url, verifyXpath, descendantXpaths, ancestorXpaths, royaltyXpaths)

    # TODO write to file
    print(urls)

