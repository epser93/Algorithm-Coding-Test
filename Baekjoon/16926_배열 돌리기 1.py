def rotate():
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visit = [[0 for _ in range(M)] for _ in range(N)]
    row, col = 0, 0
    while 1:
        if visit[row][col] == 1:
            break
        prev = board[row][col]
        for i in range(4):
            while 1:
                if 0 > row + dx[i] or row + dx[i] >= N or 0 > col + dy[i] or col + dy[i] >= M or visit[row+dx[i]][col+dy[i]] != 0:
                    break
                row += dx[i]
                col += dy[i]
                visit[row][col] = 1
                board[row][col], prev = prev, board[row][col]
        row += 1
        col += 1
         

N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
for _ in range(R):
    rotate()
for elm in board:
    print(*elm)