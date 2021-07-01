def find():
    for i in range(N-1):
        if weights[i] > C:
            return 0
        visit[i] = 1
        if weights[i] == C:
            return 1
        for j in range(i+1, N):
            visit[j] = 1
            if weights[i] + weights[j] == C:
                return 1
            remain = C - weights[i] - weights[j]
            if weightsDict.get(remain, -1) >= 0 and not visit[weightsDict.get(remain)]:
                return 1
            visit[j] = 0
        visit[i] = 0
    return 0

N, C = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()
weightsDict = {}
visit = [0] * N
for idx, weight in enumerate(weights):
    weightsDict[weight] = idx
print(find())

