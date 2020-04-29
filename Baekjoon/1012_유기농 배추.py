import sys
sys.setrecursionlimit(10**6)

def dfs(y, x):
    dx = [1,-1,0,0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        if 0 <= new_y < sero and 0 <= new_x < garo and mapp[new_y][new_x] == 1:
            mapp[new_y][new_x] = 0
            dfs(new_y, new_x)

for t in range(1, int(input())+1):
    garo, sero, baechu = map(int,input().split())
    mapp = [[0 for _ in range(garo)] for _ in range(sero)]
    cnt = 0
    for i in range(baechu):
        x, y = map(int,input().split())
        mapp[y][x] = 1

    for i in range(sero):
        for j in range(garo):
            if mapp[i][j] == 1:
                cnt += 1
                mapp[i][j] = 0
                dfs(i,j)
    print(cnt)
