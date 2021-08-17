def dfs(idx, result):
    if idx == M:
        print(*result)
        return
    for number in numbers:
        if number not in result:
            dfs(idx+1, result+[number])

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
dfs(0, [])