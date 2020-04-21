def BFS(row,col):
    global cnt
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = [(row,col)]
    while 1:
        if len(q) == 0:
            break
        qq = q.pop(0)
        for i in range(4):
            if 0 <= qq[0] + dx[i] < N and 0 <= qq[1] + dy[i] < N and board[qq[0]+dx[i]][qq[1]+dy[i]] == 1:
                board[qq[0]+dx[i]][qq[1]+dy[i]] = 0
                q.append((qq[0]+dx[i],qq[1]+dy[i]))
                cnt += 1
    return cnt

N = int(input())
board = []
arr = []
for _ in range(N):
    board.append(list(map(int,input())))
for x in range(N):
    for y in range(N):
        cnt = 0
        if board[x][y] == 1:
            cnt += 1
            board[x][y] = 0 
            arr.append(BFS(x,y))
sort_arr = sorted(arr)
print(len(sort_arr))
for j in range(len(sort_arr)):
    print(sort_arr[j])