import heapq
import copy

def down(m, n):
    for col in range(n):
        zeroPositions = []
        for row in range(m-1, -1, -1):
            if boards[row][col] == "0":
                heapq.heappush(zeroPositions,(-row, row))
                continue
            if zeroPositions:
                zeroRow = heapq.heappop(zeroPositions)[1]
                downTarget = boards[row][col]
                boards[zeroRow][col] = downTarget
                boards[row][col] = "0"
                heapq.heappush(zeroPositions, (-row, row)) 

def check(row, col):
    target = boards[row][col]
    for dRow in range(2):
        for dcol in range(2):
            if boards[row + dRow][col + dcol] != target:
                return False
    return True

def find(m, n):
    position = []
    for col in range(n-1):
        for row in range(m-1):
            if check(row, col):
                position.append((row, col))
    return position

def delete(positions):
    for row, col in positions:
        for dRow in range(2):
            for dCol in range(2):
                boards[row + dRow][col + dCol] = "0"

def calculate(m, n):
    cnt = 0
    for row in range(m):
        for col in range(n):
            if boards[row][col] == "0":
                cnt += 1
    return cnt

def solution(m, n, board):
    global boards
    boards = list(map(list, board))
    while 1:
        prevBoard = copy.deepcopy(boards)
        positions = find(m,n)
        delete(positions)
        down(m, n)
        if boards == prevBoard:
            break
    answer = calculate(m, n)
    return answer

if __name__ == "__main__":
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
    print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))