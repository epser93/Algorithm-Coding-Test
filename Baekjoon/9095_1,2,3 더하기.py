def dfs(summ):
    global cnt
    if summ > n:
        return
    if summ == n:
        cnt += 1
        return
    for i in range(1,4):
        new_sum = summ + i
        dfs(new_sum)

for t in range(1, int(input())+1):
    n = int(input())
    cnt = 0
    dfs(0)
    print(cnt)
