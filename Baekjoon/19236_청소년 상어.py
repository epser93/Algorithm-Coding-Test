# https://www.acmicpc.net/problem/19236

import copy

def is_not_wall(x, y):
    if y >= 0 and y < 4 and x >= 0 and x < 4:
        return 1
    return 0

def find_fish_start(fish, board):
    for x in range(4):
        for y in range(4):
            if board[x][y][0] == fish:
                return [x, y]
    return 500

def move_fish(maps):
    for i in range(1, 17):
        fish_position = find_fish_start(i, maps)
        if fish_position != 500:
            x, y = fish_position[0], fish_position[1]
            for j in range(8):
                direction = (maps[x][y][1] - 1 + j) % 8
                next_x = x + dx[direction]
                next_y = y + dy[direction]
                if is_not_wall(next_x, next_y) and 0 <= maps[next_x][next_y][0] <= 16:
                    maps[x][y][1] = direction + 1
                    maps[x][y], maps[next_x][next_y] = maps[next_x][next_y], maps[x][y]
                    break
    return maps

def move_shark(maps, shark_x, shark_y):
    direction = maps[shark_x][shark_y][1]
    position = []
    for _ in range(4):
        shark_x += dx[direction - 1]
        shark_y += dy[direction - 1]

        if is_not_wall(shark_x, shark_y) and 1 <= maps[shark_x][shark_y][0] <= 16:
            position.append([shark_x, shark_y])
    
    return position

def dfs(maps, x, y, summ):
    global result
    board = copy.deepcopy(maps)
    summ += board[x][y][0]
    board[x][y][0] = 77

    new_board = move_fish(board)
    shark_position = move_shark(new_board, x, y)

    if len(shark_position) == 0:
        if summ >= result:
            result = summ
            return
    else:
        board[x][y][0] = 0
        for position in shark_position:
            shark_x, shark_y = position[0], position[1]
            dfs(new_board, shark_x, shark_y, summ)

mapp = [[] for _ in range(4)]

for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(0,8,2):
        mapp[i].append([temp[j], temp[j+1]])

dy = [0, -1, -1, -1, 0, 1, 1, 1] # 상 , 왼상, 왼, 왼하, 하, 오하, 오, 오상
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

result = -99999999999999

dfs(mapp, 0, 0, 0)

print(result)
