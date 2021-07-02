from collections import deque

def isWall(row, col):
    if 0 <= row < l and 0 <= col < l:
        return False
    return True

for _ in range(int(input())):
    l = int(input())
    startX, startY = map(int, input().split())
    targetX, targetY= map(int, input().split())
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    visit = [[0 for _ in range(l)] for _ in range(l)]
    queue = deque([[startX, startY, 0]])
    result = 0

    while queue:
        x, y, cnt = queue.popleft()
        if x == targetX and y == targetY:
            result = cnt
            break
        for i in range(8):
            newX, newY = x + dx[i], y + dy[i]
            if not isWall(newX, newY) and not visit[newX][newY]:
                visit[newX][newY] = 1
                queue.append([newX, newY, cnt+1])
    print(result)