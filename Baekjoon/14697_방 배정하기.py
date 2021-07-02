def dfs(idx, result):
    global rule
    if idx == 3:
        if result == rule[-1]:
            print(1)
            exit()
        return
    for i in range(0, 51):
        dfs(idx+1, result + rule[idx] * i)

rule = list(map(int, input().split()))
dfs(0, 0)
print(0)