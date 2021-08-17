def dfs(idx, result):
    if idx == M:
        print(*result)
        return
    for num in numbers:
        dfs(idx+1, result+[num])

N, M = map(int, input().split())
numbers = [x for x in range(1, N+1)]
dfs(0, [])