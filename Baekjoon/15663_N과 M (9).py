def dfs(idx, result):
    if idx == M:
        result = tuple(result)
        if not resultVisit.get(result):
            resultVisit[result] = 1
            print(*result)
        return
    for i in range(len(numbers)):
        if not visit[i]:
            visit[i] = 1
            dfs(idx+1, result+[numbers[i]])
            visit[i] = 0

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
visit = [0] * len(numbers)
resultVisit = {}
dfs(0, [])