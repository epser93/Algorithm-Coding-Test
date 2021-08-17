def dfs(idx, prev, result):
    if idx == M:
        print(*result)
        return
    for i in range(prev, len(numbers)):
        dfs(idx+1, i+1, result+[numbers[i]])
        
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
dfs(0, 0, [])