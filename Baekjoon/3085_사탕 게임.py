def isWall(row, col, N):
    if 0 <= row < N and 0 <= col < N:
        return False
    return True

def findMaxByRow(row):
    global board, maxCnt
    start = board[row][0]
    cnt = 1
    for i in range(1, N):
        if start == board[row][i]:
            cnt += 1
        else:
            cnt = 1
            start = board[row][i]
        if cnt > maxCnt:
            maxCnt = cnt

def findMaxByCol(col):
    global board, maxCnt
    start = board[0][col]
    cnt = 1
    for i in range(1, N):
        if start == board[i][col]:
            cnt += 1
        else:
            cnt = 1
            start = board[i][col]
        if cnt > maxCnt:
            maxCnt = cnt

N = int(input())
board = [list(input()) for _ in range(N)]
maxCnt = float('-inf')
dx = [0, 0, -1, 1] # 상 하 좌 우
dy = [-1, 1, 0, 0]

for row in range(N):
    for col in range(N):
        for i in range(4):
            if not isWall(row + dx[i], col + dy[i], N):
                board[row][col], board[row + dx[i]][col + dy[i]] = board[row + dx[i]][col + dy[i]], board[row][col]
                findMaxByRow(row)
                findMaxByCol(col)
                findMaxByRow(row+dx[i])
                findMaxByCol(col+dy[i])
                board[row][col], board[row + dx[i]][col + dy[i]] = board[row + dx[i]][col + dy[i]], board[row][col]

print(maxCnt)
