def isCorrectByRow(board):
    for rowBoard in board:
        if len(set(rowBoard)) != 9:
            return False
    return True

def isCorrectByCol(board):
    rotateBoard = []
    for elm in zip(*board):
        rotateBoard.append(elm)
    if isCorrectByRow(rotateBoard) == False:
        return False
    return True

def isCorrectBy33(board):
    for x in range(0,9,3):
        for y in range(0,9,3):
            numList = set()
            for i in range(3):
                for j in range(3):
                    numList.add(board[x + i][y + j])
            if len(numList) != 9:
                return False
    return True

def check(board):
    if isCorrectByRow(board) and isCorrectByCol(board) and isCorrectBy33(board):
        return "CORRECT"
    return "INCORRECT"

n = int(input())
for loop in range(n):
    board = [list(map(int, input().split())) for _ in range(9)]
    if loop != n - 1:
        space = input()
    print("Case {}: {}".format(loop + 1, check(board)))

