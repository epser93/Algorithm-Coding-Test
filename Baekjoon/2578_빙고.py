def findIdx(number):
    for row in range(5):
        for col in range(5):
            if board[row][col] == number:
                return (row, col)

def rowCheck():
    cnt = 0
    for row in range(5):
        for col in range(5):
            if not visit[row][col]:
                break
        else:
            cnt += 1
    return cnt

def colCheck():
    cnt = 0
    for col in range(5):
        for row in range(5):
            if not visit[row][col]:
                break
        else:
            cnt += 1
    return cnt 

def diagonalCheck():
    cnt = 0
    for i in range(5):
        if not visit[i][i]:
            break
    else:
        cnt += 1
    for j in range(5):
        if not visit[4-j][j]:
            break
    else:
        cnt += 1
    return cnt

def check():
    return rowCheck() + colCheck() + diagonalCheck()

board = [list(map(int, input().split())) for _ in range(5)]
sequences = [list(map(int, input().split())) for _ in range(5)]
visit = [[0 for _ in range(5)] for _ in range(5)]
count = 0
for sequence in sequences:
    for number in sequence:
        count += 1
        row, col = findIdx(number)
        visit[row][col] = 1
        bingo = check()
        if bingo >= 3:
            print(count)
            exit()