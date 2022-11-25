
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def crawlerQuality(listOfPairs):
    answer = dict()
    valid_finds = list()
    number_of_crawls = 0
    for i in listOfPairs:
        if i[2] == 1:
            number_of_crawls += 1
            if i[1] in valid_family_members:
                valid_finds.append(i[1])
    inter = len(intersection(valid_find,valid_family_members))
    answer["precision"] = inter / number_of_crawls
    answer["recall"] = inter / (len(valid_family_members)-1)
    answer["F1"] = 2 * answer["precision"] * answer["recall"] / (answer["precision"] + answer["recall"])
    return answer


