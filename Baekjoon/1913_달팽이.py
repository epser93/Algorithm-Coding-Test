N = int(input())
target = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
dx = [0, 1, 0, -1] # 우 하 좌 상
dy = [1, 0, -1, 0]

targetPosition = []
num = 2
cnt = 2
row, col = N // 2, N // 2
board[row][col] = 1
while 1:
    if num == N*N + 1:
        break
    row += -1
    col += -1
    for i in range(4):
        for j in range(cnt):
            row += dx[i]
            col += dy[i]
            board[row][col] = num
            if num == target:
                targetPosition.append([row+1, col+1])
            num += 1
    cnt += 2

for elm in board:
    print(*elm)
if targetPosition:
    print(*targetPosition[0])
elif target == 1:
    print(*[N // 2 + 1, N // 2 + 1])