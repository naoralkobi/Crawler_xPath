import requests
import lxml.html
import lxml.etree
import time

from Q4 import crawlerQuality

"""
    this class represent Crawler action
"""


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
        self._pairs = []

    def start_crawling(self):
        limit_crawling = 0
        while True:
            # exit
            # print("size is " + str(limit_crawling))
            if limit_crawling == self._max_size:
                break
            limit_crawling += 1
            # check if it is royalty member.
            if not is_member(self._current_url.get_url(), verifyXpath):
                print(self._current_url.get_url() + " is not royalty member")
                new_page = self.get_next()
                while new_page.get_is_crawled() == 1:
                    new_page = self.get_next()
                self.set_current_url(new_page)
                continue
            source = self._current_url.get_source()
            self.update_pair(source, self._current_url.get_url())
            self._urls.add(self._current_url.get_url())
            # print(self._current_url.get_url() + " great he is royalty member")
            self.crawl()

    def update_pair(self, source, target):
        for pair in self._pairs:
            if pair[0] == source and pair[1] == target:
                pair[2] = 1

    def crawl(self):
        self._current_url.set_is_crawled()

        # reading html.
        response = requests.get(self._current_url.get_url())
        html = response.text
        time.sleep(3)

        descendants = self.get_links(self._descendantXpaths, html)
        add_item_to_set(self._current_url.get_descendants(), descendants)

        ancestors = self.get_links(self._ancestorXpaths, html)
        add_item_to_set(self._current_url.get_ancestors(), ancestors)

        others = self.get_links(self._royaltyXpaths, html)
        add_item_to_set(self._current_url.get_other_royalties(), others)

        new_page = self.get_next()
        while new_page.get_is_crawled() == 1:
            new_page = self.get_next()
        self.set_current_url(new_page)

    def add_pair(self, source, target):
        self._pairs.append([source, target, 0])

    def get_pairs(self):
        return self._pairs

    def get_links(self, xpaths, html):
        results = []
        doc = lxml.html.fromstring(html)
        for xpath in xpaths:
            for domain in doc.xpath(xpath):
                link = fix_url(domain)
                self._pages_set.add(Url(link, self._current_url.get_url()))
                results.append(link)
                self.add_pair(self._current_url.get_url(), link)
        return results

    def set_current_url(self, new_url):
        self._current_url = new_url

    def get_next(self):
        if self._pages_set:
            item = list(self._pages_set)[0]
            for page in self._pages_set:
                if page.get_descendant_counter() < item.get_descendant_counter():
                    item = page
            self._pages_set.remove(item)
            return item
        return None

    def get_urls(self):
        return self._urls


"""
    this class represent Url.
"""


class Url:
    def __init__(self, url, source):
        self._url = url
        self._descendants = set()
        self._descendant_counter = 0
        self._ancestor = set()
        self._other_royalty = set()
        self._is_crawled = 0
        self._source = source

    def get_source(self):
        return self._source

    def set_is_crawled(self):
        self._is_crawled = 1

    def get_is_crawled(self):
        return self._is_crawled

    def get_descendants(self):
        return self._descendants

    def get_ancestors(self):
        return self._ancestor

    def get_other_royalties(self):
        return self._other_royalty

    def get_descendant_counter(self):
        return self._descendant_counter

    def get_url(self):
        return self._url


def add_item_to_set(current_set, items):
    for item in items:
        current_set.add(item)


"""
    this function build correct url.
"""


def fix_url(url):
    #  (url)
    if url.startswith('https://en.wikipedia.org/'):
        return url
    else:
        return 'https://en.wikipedia.org/' + url


"""
this function get url and using verifyXpath to check if it is real royalty family.
"""


def is_member(url, verifyXpath):
    url = fix_url(url)
    response = requests.get(url)
    html = response.text
    doc = lxml.html.fromstring(html)
    return doc.xpath(verifyXpath)


def britishCrawler(url, verifyXpath, descendantXpaths, ancestorXpaths, royaltyXpaths):
    start_url = Url(url, url)
    crawler = Crawler(start_url, verifyXpath, descendantXpaths, ancestorXpaths, royaltyXpaths)
    # start crawling
    crawler.start_crawling()
    print("finish crawling..")
    print(crawler.get_pairs())
    return crawler.get_pairs()


if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/Charles_III"

    verifyXpath = "//table[@class = 'infobox vcard']/following-sibling::p[1]//text()[contains(.,'of the United Kingdom')] |" \
                  " //table[@class = 'infobox vcard']/following-sibling::p[1]//text()[contains(.,'succession to the British throne')] |" \
                  "//table[@class = 'infobox vcard']/following-sibling::p[1]//text()[contains(.,'heir apparent')]"

    descendantXpaths = ["//table[@class = 'infobox vcard']/tbody/tr/th[contains(text(),'Issue')]/..//a""/@href[contains(., 'wiki')]"]

    ancestorXpaths = [
        "//table[@class = 'infobox vcard']/tbody/tr/th[contains(text(),'Father')]/..//a/@href[contains(., 'wiki')]",
        "//table[@class = 'infobox vcard']/tbody/tr/th[contains(text(),'Mother')]/..//a/@href[contains(., 'wiki')]"]

    royaltyXpaths = [
        "//table[@class = 'infobox vcard']/tbody/tr/th[contains(text(),'Predecessor')]/..//a/@href[contains(., 'wiki')]",
        "//table[@class = 'infobox vcard']/tbody/tr/th[contains(text(),'Successor')]/..//a/@href[contains(., 'wiki')]",
        "//td[@class = 'sidebar-content']/ul//li//a[1]//@href[contains(.,'/wiki/')]"]

    urls = britishCrawler(url, verifyXpath, descendantXpaths, ancestorXpaths, royaltyXpaths)

    print(crawlerQuality(urls))

    # TODO write to file
    # print(urls)
