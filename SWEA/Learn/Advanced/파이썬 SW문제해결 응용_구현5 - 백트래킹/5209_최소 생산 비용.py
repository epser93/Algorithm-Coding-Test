def cost(idx, summ):
    global min_cost
    if summ > min_cost:
        return
    if idx == N:
        if summ < min_cost:
            min_cost = summ
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            cost(idx+1, summ+costMap[idx][i])
            visit[i] = 0

for t in range(1, int(input())+1):
    N = int(input())
    costMap = [list(map(int,input().split())) for _ in range(N)]
    visit = [0 for _ in range(N)]
    min_cost = 9999999999999
    cost(0,0)
    print('#{} {}'.format(t,min_cost))