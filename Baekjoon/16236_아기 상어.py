from collections import deque

def findStart(N):
    global board
    for row in range(N):
        for col in range(N):
            if board[row][col] == 9:
                return (row, col)

def isWall(row, col, N, sharkSize):
    global board
    if 0 <= row < N and 0 <= col < N and board[row][col] <= sharkSize:
        return False
    return True

def canIEat(row, col, sharkSize):
    global board
    if 0< board[row][col] < sharkSize:
        return True
    return False

def bfs(row, col, N, sharkSize):
    global dx, dy
    queue = deque([[row, col, 1]]) # 행 렬 거리
    distanceBoard = [[0 for _ in range(N)] for _ in range(N)]
    visit = [[0 for _ in range(N)] for _ in range(N)]
    while queue:
        row, col, distance = queue.popleft()
        for i in range(4):
            newRow, newCol = row+dx[i], col+dy[i]
            if not isWall(newRow, newCol, N, sharkSize) and not visit[newRow][newCol]:
                if canIEat(newRow, newCol, sharkSize):
                    distanceBoard[newRow][newCol] = distance
                queue.append([newRow, newCol, distance+1])
                visit[newRow][newCol] = 1
    return distanceBoard

def findFood(distanceBoard, N):
    minDistance = float('inf')
    targetRow, targetCol = -1, -1
    for row in range(N):
        for col in range(N):
            if 0 < distanceBoard[row][col] < minDistance:
                minDistance = distanceBoard[row][col]
                targetRow, targetCol = row, col
    if targetRow != -1:
        return (targetRow, targetCol, minDistance)
    return 0

def canIGrow(growCnt, sharkSize):
    if growCnt == sharkSize:
        return (0, sharkSize+1)
    return growCnt, sharkSize

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]
row, col = findStart(N)
board[row][col] = 0
sharkSize = 2
result = 0
growCnt = 0
while 1:
    foodLocation = findFood(bfs(row, col, N, sharkSize), N)
    if not foodLocation:
        break
    row, col, distance = foodLocation
    board[row][col] = 0
    result += distance
    growCnt, sharkSize = canIGrow(growCnt+1, sharkSize)
print(result)