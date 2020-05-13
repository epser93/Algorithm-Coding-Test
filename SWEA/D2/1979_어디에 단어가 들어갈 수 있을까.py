def check_right(x,y):
    cnt = 1
    while 1:
        if x >= 0 and x < N and y + 1 >= 0 and y + 1 < N and game_map[x][y+1] == 1:
            cnt += 1
            y += 1
        else: break
    if x >= 0 and x < N and y - cnt >= 0 and y - cnt < N and game_map[x][y-cnt] == 1:
        cnt += 100
    if cnt == K:
        return True
    else: return False

def check_down(x,y):
    cnt = 1
    while 1:
        if x + 1 >= 0 and x + 1 < N and y >= 0 and y < N and game_map[x+1][y] == 1:
            cnt += 1
            x += 1
        else: break
    if x - cnt >= 0 and x -cnt < N and y >= 0 and y < N and game_map[x-cnt][y] == 1:
        cnt += 100
    if cnt == K:
        return True
    else: return False

T = int(input())
for t in range(T):
    N, K = map(int,input().split())
    game_map = []
    result = 0
    for _ in range(N):
        game_map.append(list(map(int,input().split())))
    for x in range(N):
        for y in range(N):
            if game_map[x][y] == 0:
                continue
            if check_right(x,y):
                result += 1
            if check_down(x,y):
                result += 1
    print('#{} {}'.format(t+1,result))