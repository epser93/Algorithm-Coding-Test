def getDistance(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

def solution(numbers, hand):
    keyPad = {
        1 : (0,0),
        2 : (0,1),
        3 : (0,2),
        4 : (1,0),
        5 : (1,1),
        6 : (1,2),
        7 : (2,0),
        8 : (2,1),
        9 : (2,2),
        0 : (3,1)
    }
    left = [1, 4, 7]
    right = [3, 6, 9]
    leftIdx = (3, 0)
    rightIdx = (3, 2)
    result = ""
    for number in numbers:
        if number in left:
            result += "L"
            leftIdx = keyPad[number]
        elif number in right:
            result += "R"
            rightIdx = keyPad[number]
        else:
            leftDistance = getDistance(leftIdx, keyPad[number])
            rightDistance = getDistance(rightIdx, keyPad[number])
            if leftDistance == rightDistance:
                if hand == "right":
                    rightIdx = keyPad[number]
                    result += "R"
                else:
                    leftIdx = keyPad[number]
                    result += "L"
            elif leftDistance < rightDistance:
                leftIdx = keyPad[number]
                result += "L"
            else:
                rightIdx = keyPad[number]
                result += "R"
    return result

if __name__ == "__main__":
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))