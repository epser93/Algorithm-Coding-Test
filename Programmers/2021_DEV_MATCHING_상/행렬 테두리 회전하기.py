def makeBoard(rows, columns):
    board = []
    num = 1
    for _ in range(rows):
        temp = []
        for _ in range(columns):
            temp.append(num)
            num += 1
        board.append(temp)
    return board

def isWall(x, y, row, col):
    if 0 <= x < row and 0 <= y < col:
        return False
    return True

def shift(x1, y1, x2, y2, row, col):
    temp = []
    dx = [0, 1, 0, -1] # 우 하 좌 상
    dy = [1, 0, -1, 0]
    nowX = x1 - 1
    nowY = y1 - 1
    tempValue = board[nowX][nowY] 

    for i in range(4):
        while 1:
            nextX = nowX + dx[i]
            nextY = nowY + dy[i]
            if isWall(nextX, nextY, row, col) or nextX < x1 - 1 or nextX > x2 - 1 or nextY < y1 - 1 or nextY > y2 - 1:
                break
            temp.append(tempValue)
            board[nextX][nextY], tempValue = tempValue, board[nextX][nextY]
            nowX = nextX
            nowY = nextY
    return min(temp)

def solution(rows, columns, queries):
    global board
    board = makeBoard(rows, columns)
    result = []
    for query in queries:
        x1, y1, x2, y2 = query
        result.append(shift(x1, y1, x2, y2, rows, columns))
    return result

if __name__=="__main__":
    print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
    print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
    print(solution(100, 97, [[1,1,100,97]]))