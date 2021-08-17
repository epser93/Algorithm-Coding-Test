N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
def dfs(idx, result):
    if idx == M:
        print(*result)
        return
    for num in numbers:
        dfs(idx+1, result+[num])
dfs(0, [])