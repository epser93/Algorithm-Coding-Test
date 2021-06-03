def solution(clothes):
    clothDict = {}
    result = 1
    for cloth, type in clothes:
        if not clothDict.get(type):
            clothDict[type] = 1
        else:
            clothDict[type] += 1

    for cnt in clothDict.values():
        result *= (cnt + 1)
    
    return result - 1

if __name__ == "__main__":
    print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
    print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))