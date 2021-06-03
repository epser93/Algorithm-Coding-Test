from collections import deque

def isWall(maps, x, y, n, m):
    if 0 <= x < n and 0 <= y < m and maps[x][y] != 0:
        return False
    return True

def solution(maps):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    n, m = len(maps), len(maps[0])
    queue = deque([[0, 0, 1]])
    maps[0][0] = 1
    while queue:
        x, y, turn = queue.popleft()
        if x == n - 1 and y == m - 1:
            return turn
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if not isWall(maps, newX, newY, n, m):
                queue.append([newX, newY, turn + 1])
                maps[newX][newY] = 0
    return -1

if __name__ == "__main__":
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))