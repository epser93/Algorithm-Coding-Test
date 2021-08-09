N = int(input())
board = [list(input()) for _ in range(N)]
current = [list(input()) for _ in range(N)]
resultBoard = [['.' for _ in range(N)] for _ in range(N)]
mineFlag = False
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for row in range(N):
    for col in range(N):
        if board[row][col] == "*" and current[row][col] == "x":
            mineFlag = True
        if current[row][col] == "x":
            cnt = 0
            for i in range(8):
                new_dx, new_dy = row + dx[i], col + dy[i]
                if 0 <= new_dx < N and 0 <= new_dy < N and board[new_dx][new_dy] == "*":
                    cnt += 1
            resultBoard[row][col] = str(cnt)

if mineFlag:
    for row in range(N):
        for col in range(N):
            if board[row][col] == "*":
                resultBoard[row][col] = "*"

for i in range(N):
    print(''.join(resultBoard[i]))