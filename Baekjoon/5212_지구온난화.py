# BOJ 5212 지구온난화
# https://www.acmicpc.net/problem/5212 

import copy

R, C = map(int, input().split())
islandMap = [list(input()) for _ in range(R)]
newIslandMap = copy.deepcopy(islandMap)

dy = [0, 0 , -1, 1] # 상하좌우
dx = [-1, 1, 0, 0]
ISLAND = 'X'
SEA = '.'
for x in range(R):
    for y in range(C):
        if islandMap[x][y] == ISLAND:
            cnt = 0
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if (new_x < 0 or new_x >= R) or (new_y < 0 or new_y >= C) or islandMap[new_x][new_y] == SEA:
                    cnt += 1
            if cnt >= 3:
                newIslandMap[x][y] = SEA

rowIndex = []
colIndex = []
for i in range(R):
    if ISLAND in newIslandMap[i]:
        rowIndex.append(i)

reverseMap = [list(reverseEl) for reverseEl in zip(*newIslandMap)]
for i in range(C):
    if ISLAND in reverseMap[i]:
        colIndex.append(i)

startRow = min(rowIndex)
endRow = max(rowIndex)
startCol = min(colIndex)
endCol = max(colIndex)
    
for x in range(startRow, endRow + 1):
    print(''.join(newIslandMap[x][startCol:endCol+1]))