def dfs(idx, before, summ):
    global min_cost
    if summ > min_cost:
        return
    if idx == N-1:
        summ += mapp[before][0]
        if summ < min_cost:
            min_cost = summ
        return
    for i in range(1,N):
        if not visit[i]:
            visit[i] = 1
            dfs(idx+1,i,summ+mapp[before][i])
            visit[i] = 0

for t in range(1, int(input())+1):
    N = int(input())
    mapp = [list(map(int,input().split())) for _ in range(N)]
    visit = [0 for _ in range(N)]
    min_cost = 999999999
    dfs(0,0,0)
    print('#{} {}'.format(t,min_cost))