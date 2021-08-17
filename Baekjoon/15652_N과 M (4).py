def dfs(idx, prev, result):
    if idx == M:
        print(*result)
        return
    for i in range(prev, len(numbers)):
        dfs(idx+1, i, result+[numbers[i]])

N, M = map(int, input().split())
numbers = [x for x in range(1, N+1)]
dfs(0, 0, [])