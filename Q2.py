import requests
import lxml.html
import lxml.etree


def is_member(url):
    response = requests.get(url)
    html = response.text
    doc = lxml.html.fromstring(html)

    x_path = "//div[@class='mw-body-content mw-content-ltr']//p//text()" \
             "[contains(.,'was Queen of the United Kingdom') or contains(.,'was King of the United Kingdom') " \
             "or contains(.,'is King of the United Kingdom')]"

    return doc.xpath(x_path)


if __name__ == '__main__':
    # print(is_member("https://en.wikipedia.org/wiki/Elizabeth_II"))
    # print(is_member("https://en.wikipedia.org/wiki/Football"))
    # print(is_member("https://en.wikipedia.org/wiki/George_VI"))
    # print(is_member("https://en.wikipedia.org/wiki/Queen_Elizabeth_The_Queen_Mother"))
    # print(is_member("https://en.wikipedia.org/wiki/Prince_Henry,_Duke_of_Gloucester"))
    # print(is_member("https://en.wikipedia.org/wiki/Princess_Alice,_Duchess_of_Gloucester"))
    # print(is_member("https://en.wikipedia.org/wiki/Prince_George,_Duke_of_Kent"))
    # print(is_member("https://en.wikipedia.org/wiki/Princess_Marina_of_Greece_and_Denmark"))
    # print(is_member("https://en.wikipedia.org/wiki/George_V"))
    # print(is_member("https://en.wikipedia.org/wiki/Mary_of_Teck"))
    # print(is_member("https://en.wikipedia.org/wiki/Prince_Philip,_Duke_of_Edinburgh"))
    print(is_member("https://en.wikipedia.org/wiki/Wallis_Simpson"))
