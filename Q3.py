import requests
import lxml.html
import lxml.etree


class Crawler:
    def __init__(self, current_url, verifyXpath, descendantXpaths, ancestorXpaths, royaltyXpaths):
        # set of class Url
        self._pages_set = set()
        # set of real Url
        self._urls = set()
        self._max_size = 30
        self._current_url = current_url
        self._verifyXpath = verifyXpath
        self._descendantXpaths = descendantXpaths
        self._ancestorXpaths = ancestorXpaths
        self._royaltyXpaths= royaltyXpaths

    def start_crawling(self):
        while True:
            # exit
            if len(self._urls) == self._max_size:
                break
            # check if it is royalty member.
            if not is_member(self._current_url.get_url(), verifyXpath):
                # print(_current_url.get_url() + "is not royalty member")
                continue
            self._urls.add(self._current_url.get_url())
            # print(self._current_url.get_url() + "great he is royalty member")
            self.crawl()

    def crawl(self):
        print("crawling")
        pass

    def get_next(self):
        if self._pages_set:
            item = list(self._pages_set)[0]
            for page in self._pages_set:
                if page.get_descendant_counter() < item.get_descendant_counter():
                    item = page
            return item
        return None

    def get_urls(self):
        return self._urls


class Url:
    def __init__(self, url):
        self._url = url
        self._descendants = set()
        self._descendant_counter = 0
        self._ancestor = set()
        self._other_royalty = set()

    def get_descendant_counter(self):
        return self._descendant_counter

    def get_url(self):
        return self._url


def add_item_to_set(current_set, item):
    current_set.add(item)

def fix_url(url):
    if url.startswith('https://en.wikipedia.org/'):
        return url
    else:
        return 'https://en.wikipedia.org/' + url


def is_member(url, verifyXpath):
    url = fix_url(url)
    response = requests.get(url)
    html = response.text
    doc = lxml.html.fromstring(html)

    # this check if his king or queen in the first p.
    x_path = "//table[@class = 'infobox vcard']/following-sibling::p[1]//text()[contains(.,'of the United Kingdom')]"

    return doc.xpath(x_path)


def britishCrawler(url, verifyXpath, descendantXpaths, ancestorXpaths, royaltyXpaths):
    start_url = Url(url)
    crawler = Crawler(start_url, verifyXpath, descendantXpaths, ancestorXpaths, royaltyXpaths)
    # start crawling
    crawler.start_crawling()
    print("finish crawling..")
    print(crawler.get_urls())


if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/Charles_III"
    # TODO need to add more cases.
    verifyXpath = "//table[@class = 'infobox vcard']//a[contains(text(), 'of the United Kingdom')]/@href[contains(., 'wiki')]"

    descendantXpaths = "//table[@class = 'infobox vcard']/tbody/tr/th[contains(text(),'Issue')]/..//a""/@href[contains(., 'wiki')]"

    ancestorXpaths = [
        "//table[@class = 'infobox vcard']/tbody/tr/th[contains(text(),'Father')]/..//a/@href[contains(., 'wiki')]",
        "//table[@class = 'infobox vcard']/tbody/tr/th[contains(text(),'Mother')]/..//a/@href[contains(., 'wiki')]"]

    royaltyXpaths = [
        "//table[@class = 'infobox vcard']/tbody/tr/th[contains(text(),'Predecessor')]/..//a/@href[contains(., 'wiki')]",
        "//table[@class = 'infobox vcard']/tbody/tr/th[contains(text(),'Successor')]/..//a/@href[contains(., 'wiki')]",
        "//td[@class = 'sidebar-content']/ul//li//a[1]//@href[contains(.,'/wiki/')]"]

    urls = britishCrawler(url, verifyXpath, descendantXpaths, ancestorXpaths, royaltyXpaths)

    # TODO write to file
    print(urls)
