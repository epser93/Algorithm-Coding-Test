def getScore(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 50:
        return "D"
    return "F"

def solution(scores):
    result = ""
    for i in range(len(scores)):
        score = 0
        maxNum = [float('-inf'), 0]
        minNum = [float('inf'), 0]
        for j in range(len(scores)):
            score += scores[j][i]
            if scores[j][i] > maxNum[0]:
                maxNum = [scores[j][i], 1]
            elif scores[j][i] == maxNum[0]:
                maxNum[1] += 1
            if scores[j][i] < minNum[0]:
                minNum = [scores[j][i], 1]
            elif scores[j][i] == minNum[0]:
                minNum[1] += 1
        if (scores[i][i] == maxNum[0] and maxNum[1] == 1) or (scores[i][i] == minNum[0] and minNum[1] == 1):
            score -= scores[i][i]
            result += getScore(score / (len(scores)-1))
        else:
            result += getScore(score / len(scores))
    return result

if __name__ == "__main__":
    print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
    print(solution([[50,90],[50,87]]))
    print(solution([[70,49,90],[68,50,38],[73,31,100]]))