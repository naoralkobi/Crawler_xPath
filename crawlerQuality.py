import requests
import lxml.html
import lxml.etree


def fix_url(url):
    #  (url)
    if url.startswith('https://en.wikipedia.org/'):
        return url
    else:
        return 'https://en.wikipedia.org/' + url


def create_p1():
    url = "https://en.wikipedia.org/wiki/Succession_to_the_British_throne"
    x_path = '//div[@class = "treeview"]//a[not(contains(@href,"File"))]/@href[contains(.,"wiki")]'

    response = requests.get(url)
    html = response.text
    doc = lxml.html.fromstring(html)
    result = []
    for url in doc.xpath(x_path):
        result.append(fix_url(url))
    return result


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def crawlerQuality(listOfPairs):
    if not listOfPairs:
        return "no crawling has been done"
    answer = dict()
    valid_finds = list()
    number_of_crawls = 0
    valid_family_members = create_p1()
    for i in listOfPairs:
        if i[2] == 1:
            number_of_crawls += 1
            if i[1] in valid_family_members:
                valid_finds.append(i[1])
    inter = len(intersection(valid_finds, valid_family_members))
    # print(inter)
    # print(len(valid_family_members))
    # print(number_of_crawls)
    answer["precision"] = inter / number_of_crawls
    answer["recall"] = inter / (len(valid_family_members)-1)
    answer["F1"] = 2 * answer["precision"] * answer["recall"] / (answer["precision"] + answer["recall"])
    return answer
