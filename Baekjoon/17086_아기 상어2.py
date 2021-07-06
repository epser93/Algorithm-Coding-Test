from collections import deque

def isWall(row, col):
    if 0 <= row < N and 0 <= col < M:
        return False
    return True

def bfs(row, col):
    global maxDistance
    dRow = [0, -1, -1, -1, 0, 1, 1, 1]
    dCol = [-1, -1, 0, 1, 1, 1, 0, -1]
    visit = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque([[row, col, 0]])
    visit[row][col] = 1
    while queue:
        x, y, cnt = queue.popleft()
        for i in range(8):
            newRow = x + dRow[i]
            newCol = y + dCol[i]
            if not isWall(newRow, newCol) and not visit[newRow][newCol]:
                if board[newRow][newCol] == 1:
                    if cnt+1 > maxDistance:
                        maxDistance = cnt+1
                    return
                visit[newRow][newCol] = 1
                queue.append([newRow, newCol, cnt+1])
            
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
maxDistance = float('-inf')
for x in range(N):
    for y in range(M):
        if board[x][y] != 1:
            bfs(x,y)

print(maxDistance)