def dfs(r,c,summ):
    global min_sum
    if summ > min_sum: # 가지치기
        return
    if r == N-1 and c == N-1:
        if summ < min_sum:
            min_sum = summ
            return
    for i in range(2):
        new_x, new_y = r+dx[i], c+dy[i]
        if 0 <= new_x < N and 0 <= new_y < N:
            new_sum = summ + mapp[new_x][new_y]
            dfs(new_x,new_y,new_sum)

for t in range(1,int(input())+1):
    N = int(input())
    mapp = [list(map(int,input().split())) for _ in range(N)]

    dx = [1,0]
    dy = [0,1]
    min_sum = 9999999999
    dfs(0,0,mapp[0][0])
    print('#{} {}'.format(t,min_sum))