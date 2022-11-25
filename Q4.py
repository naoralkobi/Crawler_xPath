
def crawlerQuality(listOfPairs):
    answer = dict()
    valid_finds = []
    for i in listOfPairs:
        if i[2] == 1:
            if i[1] in valid_family_members:
                valid_finds.append(i[1])
    answer["precision"] = valid_finds / len(listOfPairs)
    answer["recall"] = valid_finds / 43
    answer["F1"] = 2 * answer["precision"] * answer["recall"] / (answer["precision"] + answer["recall"])
    return answer


