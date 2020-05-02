def dfs(score_sum, cal_sum):
    global max_score
    for i in range(N):
        if cal_sum + ingredient[i][1] > L:
            if score_sum >= max_score:
                max_score = score_sum 
            return
        if not visit[i] and cal_sum + ingredient[i][1] <= L:
            visit[i] = 1
            dfs(score_sum + ingredient[i][0], cal_sum + ingredient[i][1])
            visit[i] = 0

for t in range(1, int(input())+1):
    N, L = map(int,input().split())
    ingredient = []
    for _ in range(N):
        score, cal = map(int,input().split())
        ingredient.append([score, cal])

    visit = [0 for _ in range(N)]
    max_score = -99999999
    dfs(0,0)
    print('#{} {}'.format(t,max_score))