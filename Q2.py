import requests
import lxml.html
import lxml.etree
"""
    this method is checking if the url is member of the royal family.
"""


def is_member(url):
    response = requests.get(url)
    html = response.text
    doc = lxml.html.fromstring(html)

    # this check if his king or queen in the first p.
    verifyXpath = "//table[@class = 'infobox vcard']/following-sibling::p[1]//text()[contains(.,'of the United Kingdom')] |" \
                  " //table[@class = 'infobox biography vcard' or @class = 'infobox vcard']/following-sibling::p[1]//text()[contains(.,'succession to the British throne')] |" \
                  "//table[@class = 'infobox vcard']/following-sibling::p[1]//text()[contains(.,'heir apparent')]"

    return doc.xpath(verifyXpath)


if __name__ == '__main__':
    print(is_member("https://en.wikipedia.org/wiki/Princess_Alice,_Duchess_of_Gloucester"))  # no
    print(is_member("https://en.wikipedia.org/wiki/Elizabeth_II"))  # yes
    print(is_member("https://en.wikipedia.org/wiki/Football"))  # no
    print(is_member("https://en.wikipedia.org/wiki/George_VI"))   # yes
    print(is_member("https://en.wikipedia.org/wiki/Queen_Elizabeth_The_Queen_Mother"))   # yes
    print(is_member("https://en.wikipedia.org/wiki/Prince_Henry,_Duke_of_Gloucester"))  # ??
    print(is_member("https://en.wikipedia.org/wiki/Prince_George,_Duke_of_Kent"))
    print(is_member("https://en.wikipedia.org/wiki/Princess_Marina_of_Greece_and_Denmark"))
    print(is_member("https://en.wikipedia.org/wiki/George_V")) # yes
    print(is_member("https://en.wikipedia.org/wiki/Mary_of_Teck")) # yes
    print(is_member("https://en.wikipedia.org/wiki/Prince_Philip,_Duke_of_Edinburgh"))
    print(is_member("https://en.wikipedia.org/wiki/Wallis_Simpson"))
    print(is_member("https://en.wikipedia.org/wiki/Archie_Mountbatten-Windsor")) # yes
