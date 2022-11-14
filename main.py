import requests
import lxml.etree


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/Charles_III"
    page = requests.get(url)
    doc = lxml.etree.fromstring(page.content)
    print(doc)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
