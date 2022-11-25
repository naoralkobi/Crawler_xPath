import requests
import lxml.html
import lxml.etree
"""
    this x_path will print only urls of royal family.
"""

if __name__ == '__main__':
    # get the html of the page
    url1 = "https://en.wikipedia.org/wiki/George_V"
    url2 = "https://en.wikipedia.org/wiki/Charles_III"
    url3 = "https://en.wikipedia.org/wiki/Prince_Henry,_Duke_of_Gloucester"
    url4 = "https://en.wikipedia.org/wiki/Elizabeth_II"
    url5 = "https://en.wikipedia.org/wiki/Katharine,_Duchess_of_Kent"
    url6 = "https://en.wikipedia.org/wiki/Birgitte,_Duchess_of_Gloucester"
    url7 = "https://en.wikipedia.org/wiki/Queen_Elizabeth_The_Queen_Mother"
    url8 = "https://en.wikipedia.org/wiki/Prince_George,_Duke_of_Kent"
    url9 = "https://en.wikipedia.org/wiki/William,_Prince_of_Wales"

    response = requests.get(url2)
    html = response.text
    doc = lxml.html.fromstring(html)
    x_path = ""
    """
    this will print Descendants(children).
    """
    x_path1 = "//table[@class='wikitable plainrowheaders']//th//@href[contains(.,'/wiki/')]"
    """
        this will print children of children.
        TODO need to check about different tables.
    """
    x_path2 = "//table[@class='wikitable plainrowheaders']//tr//td[4]//@href[contains(.,'/wiki/')]"
    """
        this will print his Ancestors.
    """
    x_path3 = "//table[@class='ahnentafel']//td//text()[contains(.,'of the United Kingdom')]/..//@href[contains(.,'/wiki/')]"
    """
        this will print the royal family.
    """
    x_path4 = "//td[@class = 'sidebar-content']/ul//li//a[1]//@href[contains(.,'/wiki/')]"
    """
        this will print his Predecessor and Successor
    """
    x_path5 = "//table[@class = 'infobox vcard']/tbody/tr/th[contains(text(),'Predecessor') or contains(text(),'Successor')]/..//a/@href[contains(., 'wiki')]"

    #  [contains(.,'of the United Kingdom')])
    x_path = "//table[@class = 'infobox vcard']/following-sibling::p[1]//text()"

    x_path = "//div[@class='plainlist']//a//text()[contains(.,'Windsor')]/..//@href[contains(.,'/wiki/')]"

    # if 'Windsor' in x_path and 'by marriage' not in x_path:
    #     return x_path
    # else:
    #     return None

    for url in doc.xpath(x_path):
        print(url)

