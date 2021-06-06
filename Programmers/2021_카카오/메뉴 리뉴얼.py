def getCombination(orders, course):
    result = []

    def generate(idx, start, end, combResult):
        if idx == end:
            result.append(''.join(sorted(combResult)))
            return
        for i in range(start, len(orders)):
            generate(idx + 1, i + 1, end, combResult + [orders[i]])

    generate(0, 0, course, [])
    return result

def getCountDict(arr):
    countDict = {}
    for elm in arr:
        if not countDict.get(elm):
            countDict[elm] = 1
        else:
            countDict[elm] += 1
    return countDict

def solution(orders, courses):
    answer = []
    for course in courses:
        combList = []
        for order in orders:
            combList.extend(getCombination(order, course))
        if not combList:
            continue
        countDict = getCountDict(combList)
        maxValue = max(countDict.values())
        for key, value in countDict.items():
            if value >= 2 and value == maxValue:
                answer.append(key)
    return sorted(answer)


if __name__ == "__main__":
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
    print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
    print(solution(["XYZ", "XWY", "WXA"], [2,3, 4]))