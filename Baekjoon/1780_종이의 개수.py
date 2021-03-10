import sys
input = sys.stdin.readline

def isFilled(startX, startY, offset):
    length = offset
    num = board[startX][startY]
    for x in range(length):
        for y in range(length):
            if board[startX + x][startY + y] != num:
                return 9
    return num

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = {
    -1 : 0,
    0 : 0,
    1: 0
}

boardList = [(0, 0, N)]
while boardList != []:
    startX, startY, offset = boardList.pop()
    chkResult = isFilled(startX, startY, offset)
    if chkResult == 9:
        prevOffset = offset
        offset = prevOffset // 3
        for i in range(startX, startX + prevOffset, offset):
            for j in range(startY, startY + prevOffset, offset):
                boardList.append((i, j, offset))
    else:
        result[chkResult] += 1

for i in result:
    print(result[i])
