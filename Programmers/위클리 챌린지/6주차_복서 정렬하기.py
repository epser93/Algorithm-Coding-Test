def calculateWinRate(myIdx, head2heads, weight):
    win, weightWin, totalPlay = 0, 0, 0
    for idx, head2head in enumerate(head2heads):
        if head2head != "N":
            totalPlay += 1
        if head2head == "W":
            win += 1
            if weight[myIdx] < weight[idx]:
                weightWin += 1
    if totalPlay == 0:
        return 0, weightWin
    return win / totalPlay, weightWin

def solution(weights, head2head):
    boxerInfos, answer = [], []
    for i in range(len(weights)):
        winRate, weightWinCnt = calculateWinRate(i, head2head[i], weights)
        boxerInfos.append((winRate, weightWinCnt, weights[i], i+1))
    boxerInfos.sort(key = lambda x : (-x[0], -x[1], -x[2], x[3]))
    for boxerInfo in boxerInfos:
        answer.append(boxerInfo[-1])
    return answer

print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]))
print(solution([145,92,86], ["NLW","WNL","LWN"]))
print(solution([60,70,60], ["NNN","NNN","NNN"]))