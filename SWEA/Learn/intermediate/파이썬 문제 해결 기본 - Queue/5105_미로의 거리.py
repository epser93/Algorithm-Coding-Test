def bfs(x,y):
    global cnt
    cnt = -1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    queue = [(x,y)]
    mapp[x][y] = 1
    while queue:
        for _ in range(len(queue)):
            q = queue.pop(0)
            if mapp[q[0]][q[1]] == 3:
                return 
            mapp[q[0]][q[1]] = 1
            for i in range(4):
                if 0 <= q[0] + dx[i] < N and 0 <= q[1]+dy[i] < N and mapp[q[0]+dx[i]][q[1]+dy[i]] != 1:
                    queue.append((q[0]+dx[i],q[1]+dy[i]))
        cnt += 1 
    cnt = 0
    return
    
for t in range(int(input())):
    N = int(input())
    mapp = [list(map(int,input())) for _ in range(N)]
    chk = 0
    for i in range(N):
        for j in range(N):
            if mapp[i][j] == 2:
                bfs(i,j)
                chk = 1
                break
        if chk == 1:
            break

    print('#{} {}'.format(t+1,cnt))

