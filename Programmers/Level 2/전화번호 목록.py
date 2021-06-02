def solution(phone_number):
    numberDict = {}
    phone_number = sorted(phone_number, key=lambda x : len(x))
    for number in phone_number:
        for idx in range(len(number)):
            if numberDict.get(number[:idx+1]):
                return False
        numberDict[number] = 1
    return True

if __name__ == "__main__":
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123","456","789"]))
    print(solution(["12","123","1235","567","88"]))