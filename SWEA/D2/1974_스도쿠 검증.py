# 행 검증
def row(arr):
    for x in range(9):
        arr =[]
        check = 0
        for y in range(9):
            if game_map[x][y] in arr:
                return 0
            else:
                arr.append(game_map[x][y])
    return 1

# 열 검증
def col(arr):
    for y in range(9):
        arr =[]
        check = 0
        for x in range(9):
            if game_map[x][y] in arr:
                return 0
            else:
                arr.append(game_map[x][y])
    return 1

# Square 검증
def square(arr):
    for j in range(0,7,3):
        for i in range(0,7,3):
            arr = []
            for x in range(i,i+3):
                for y in range(j,j+3):
                    if game_map[x][y] in arr:
                        return 0
                    else: arr.append(game_map[x][y])
    return 1

T = int(input())
for t in range(T):
    game_map = []
    arr = []
    for _ in range(9):
        game_map.append(list(map(int,input().split())))
    if square(arr) and col(arr) and row(arr):
        print('#{} {}'.format(t+1,1))
    else:
        print('#{} {}'.format(t+1,0))