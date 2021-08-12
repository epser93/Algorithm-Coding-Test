def rotate45():
    prev = []
    for i in range(n):
        prev.append(board[i][i])
    for i in range(n):
        board[i][((n+1)//2)-1], prev[i] = prev[i], board[i][((n+1)//2)-1]
    for i in range(n):
        board[i][n-1-i], prev[i] = prev[i], board[i][n-1-i]
    for i in range(n):
        board[((n+1)//2)-1][n-1-i], prev[i] = prev[i], board[((n+1)//2)-1][n-1-i]
    for i in range(n):
        board[n-1-i][n-1-i] = prev[i]

def rotateMinus45():
    prev = []
    for i in range(n):
        prev.append(board[i][((n+1)//2)-1])
    for i in range(n):
        board[i][i], prev[i] = prev[i], board[i][i]
    for i in range(n):
        board[((n+1)//2)-1][i], prev[i] = prev[i], board[((n+1)//2)-1][i]
    for i in range(n):
        board[n-1-i][i], prev[i] = prev[i], board[n-1-i][i]
    for i in range(n):
        board[n-1-i][((n+1)//2)-1] = prev[i]

T = int(input())
for _ in range(T):
    n, degree = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    if degree >= 0:
        times = (degree // 45) % 8
        for _ in range(times):
            rotate45()
    else:
        times = (-degree // 45) % 8
        for _ in range(times):
            rotateMinus45()
    for elm in board:
        print(*elm)