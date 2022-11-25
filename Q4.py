import requests
import lxml.html
import lxml.etree

def crawlerQuality(listOfPairs):
    answer = dict()
    valid_finds = 0
    for i in listOfPairs:
        if i[2]==0:
            valid_finds+=1
    answer["precision"]=valid_finds/len(listOfPairs)
    answer["recall"]=valid_finds/43
    answer["F1"]=2*answer["precision"]*answer["recall"]/(answer["precision"]+ answer["recall"])