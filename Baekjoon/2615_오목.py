def checkPrev(row,col,target,idx):
    back_dx = [0, -1, -1, 1]
    back_dy = [-1, -1, 0, -1]
    back_row, back_col = row + back_dx[idx], col + back_dy[idx]
    if 0 <= back_row < 19 and 0 <= back_col < 19:
        if board[back_row][back_col] == target:
            return True
    return False

def play():
    dx = [0, 1, 1, -1]
    dy = [1, 1, 0, 1]
    for row in range(19):
        for col in range(19):
            if board[row][col] in [1,2]:
                target = board[row][col]
                for i in range(4):
                    if checkPrev(row, col, target, i):
                        continue
                    cnt = 1
                    new_row, new_col = row, col
                    while 1:
                        new_row += dx[i]
                        new_col += dy[i]
                        if 0 > new_row or 19 <= new_row or 0 > new_col or 19 <= new_col or board[new_row][new_col] != target :
                            break
                        cnt += 1
                    if cnt == 5:
                        return (target, row+1, col+1)
    return 0

board = [list(map(int, input().split())) for _ in range(19)]
result = play()
if result == 0:
    print(0)
else:
    print(result[0])
    print(result[1], result[2])