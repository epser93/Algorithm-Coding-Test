def solution(dartResult):
    options = {"*" : 2, "#": -1}
    margin = {"S" : 1, "D" : 2, "T" : 3}
    scoreStack = []
    result = 0
    temp = ""
    for dart in dartResult:
        if dart.isdecimal():
            temp += dart
            continue

        if temp != "":
            scoreStack.append(int(temp))
            temp = ""

        if dart == "*":
            if len(scoreStack) >= 2:
                scoreStack[-2] *= options[dart]
            scoreStack[-1] *= options[dart]

        elif dart == "#":
            scoreStack[-1] *= options[dart]
        else:
            scoreStack[-1] **= margin[dart]

    for score in scoreStack:
        result += score
    return result

if __name__ == "__main__":
    print(solution("1S2D*3T"))
    print(solution("1D2S#10S"))
    print(solution("1D2S0T"))
    print(solution("1S*2T*3S"))
    print(solution("1D#2S*3S"))
    print(solution("1T2D3D#"))
    print(solution("1D2S3T*"))