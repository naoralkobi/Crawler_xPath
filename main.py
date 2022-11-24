import requests
import lxml.html
import lxml.etree

URL2 = "https://en.wikipedia.org/wiki/Charles_III"
URL1 = "https://en.wikipedia.org/wiki/Prince_Henry,_Duke_of_Gloucester"
URL = "https://en.wikipedia.org/wiki/Elizabeth_II"

if __name__ == '__main__':
    # get the html of the page
    response = requests.get(URL)
    html = response.text
    doc = lxml.html.fromstring(html)
    x_path_list = ["//table[@class='infobox vcard']//th[contains(text(), 'Father') or contains(text(), 'Mother')]/..//@href[contains(.,'/wiki/')]",

                   "//p[contains(text(), 'sibling') or contains(text(), 'sister') or contains(text(), 'brother')]/a[contains(text(), 'Prince')]//@href[contains(.,'/wiki/')]",

                    "//table[@class='infobox vcard']//a[contains(text(), 'Prince') or contains(text(), 'King') or contains(text(), 'II')]//@href[contains(.,'/wiki/')]",

                   "//table[@class ='wikitable plainrowheaders']//td[4]//@href[contains(.,'/wiki/')]"]

    # for x_path in x_path_list:
    #     for url in doc.xpath(x_path):
    #         print(url)

    x_path1 = "//table[@class='wikitable plainrowheaders']//td//@href[contains(.,'/wiki/')]"
    x_path2 = "//table[@class='ahnentafel']//td//@href[contains(.,'/wiki/')]"
    x_path = "//div[@class='mw-body-content mw-content-ltr']//p//text()" \
             "[contains(.,'Queen of the United Kingdom') " \
             "or contains(.,'British royal family') or contains(.,'King of the United Kingdom')]"
    # x_path = "//div[@class='mw-body-content mw-content-ltr']//p//text()"
    for url in doc.xpath(x_path):
        print(url)
# "//table[@class='infobox vcard']//th[contains(text(), 'Spouse')]/..//@href[contains(.,'/wiki/')]",
# "//table[@class='infobox vcard']//th[contains(text(), 'Issue')]//..//@href[contains(.,'/wiki/')]",