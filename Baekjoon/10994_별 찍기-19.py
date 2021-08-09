def printStar(idx,row, col):
    if idx == N+1:
        return
    if idx == 1:
        board[row][col] = "*"
    else:
        for i in range(4*idx-3):
            board[row+i][col] = "*"
            board[row][col+i] = "*"
            board[row+4*idx-4][col+i] = "*"
            board[row+i][col+4*idx-4] = "*"
    printStar(idx+1, row-2, col-2)

N = int(input())
board = [[" " for _ in range(4*N-3)] for _ in range(4*N-3)]
printStar(1, (4*N-3)//2, (4*N-3)//2)
for elm in board:
    print("".join(elm))