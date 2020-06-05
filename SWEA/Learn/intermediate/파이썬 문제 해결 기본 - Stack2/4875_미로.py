def iswall(row,col):
    if 0 <= row < N and 0 <= col < N and board[row][col] != 1:
        return False
    return True

def DFS(row,col):
    global check
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        if iswall(row+dx[i],col+dy[i]):
            continue
        elif board[row+dx[i]][col+dy[i]] == 3:
            return 1      
        else:
            board[row+dx[i]][col+dy[i]] = 1
            if DFS(row+dx[i],col+dy[i]) == 1:
                return 1
            board[row+dx[i]][col+dy[i]] = 0
    return 0
T = int(input())
for t in range(T):            
    N = int(input())
    board = []
    check = 0
    for _ in range(N):
        board.append(list(map(int,input())))
    for y in range(N-1,-1,-1):
        for x in range(N-1,-1,-1):
            if board[x][y] == 2:
                board[x][y] == 0
                print('#{} {}'.format(t+1,DFS(x,y)))
                break