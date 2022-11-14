import requests
import lxml.html

URL = "https://en.wikipedia.org/wiki/Charles_III"

if __name__ == '__main__':
    # get the html of the page
    response = requests.get(URL)
    html = response.text
    doc = lxml.html.fromstring(html)
    keywords = ["I", "II", "III", "V", "IV", "VI", "VII", "VIII"]

    for word in keywords:
        for url in doc.xpath("//a/@href[contains(.,'%s')]" % word):
            print(url)



