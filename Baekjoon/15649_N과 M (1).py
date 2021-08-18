def dfs(idx, result):
    if idx == M:
        print(*result)
        return
    for i in range(len(numbers)):
        if not visit[i]:
            visit[i] = 1
            dfs(idx+1, result+[numbers[i]])
            visit[i] = 0
            
N, M = map(int, input().split())
numbers = [x for x in range(1, N+1)]
visit = [0] * N
dfs(0, [])