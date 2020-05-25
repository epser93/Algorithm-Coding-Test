def row(N,M):
    for x in range(N):
        for y in range(N-M+1):
            check = 0
            for i in range(M//2):
                if game_map[x][y+i] != game_map[x][y+M-1-i]:
                    break
                else:
                    check += 1
            if check == M//2:
                return game_map[x][y:y+M]

def col(N,M):
    for y in range(N):
        for x in range(N-M+1):
            check = 0
            for i in range(M//2):
                if game_map[x+i][y] != game_map[x+M-1-i][y]:
                    break
                else:
                    check += 1
            if check == M//2:
                map2 =""
                for j in range(M):
                    map2 += game_map[x+j][y]           
                return map2

T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    game_map =[]
    for _ in range(N):
        game_map.append(input())

    if row(N,M):
        print('#{} {}'.format(t+1, row(N,M)))
    else:
        print('#{} {}'.format(t+1,col(N,M)))