def chk(commands,X,Y):
    global idx,x,y
    idx = word_dir.index(commands) # 방향 인덱스 지정
    if 0 <= X + dx[idx] < H and 0 <= Y + dy[idx] < W and mapp[X+dx[idx]][Y+dy[idx]] == '.': # 범위 안 / 다음칸 평지라면
        mapp[X][Y] = '.' # 현재칸 평지로 만들고
        mapp[X+dx[idx]][Y+dy[idx]] = direction[idx] # 다음칸 화살표 방향 표시
        X += dx[idx]
        Y += dy[idx]
    else:
        mapp[X][Y] = direction[idx] # 평지가 아니거나 범위 밖이면 현재칸 화살표 방향만 바꿔줌
    x,y = X,Y # x,y 반환
    return

T = int(input())
for t in range(T):
    H, W = map(int,input().split())
    mapp = [list(input()) for _ in range(H)]
    N = int(input())
    command = list(input())
    direction = ['<', '^', '>', 'v']
    word_dir = ['L','U','R','D']
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    check = 0
    for y in range(W):
        for x in range(H):
            if mapp[x][y] in direction: # 시작점 탐색
                idx = direction.index(mapp[x][y]) # 방향 인덱스 지정
                for com in command: # 커맨드 하나씩 뽑아서
                    if com == 'S': # S면 슛팅
                        new_x, new_y = x,y #초기화
                        while 1:
                            new_x += dx[idx]
                            new_y += dy[idx]
                            if 0 > new_x or new_x >= H or 0 > new_y or new_y >= W: # 맵 범위 밖이면
                                break
                            elif 0<= new_x < H and 0 <= new_y < W and mapp[new_x][new_y] == '*': # 벽돌벽이면
                                mapp[new_x][new_y] = '.' # 벽돌벽 부수고 평지로 만들기
                                break
                            elif 0<= new_x < H and 0 <= new_y < W and mapp[new_x][new_y] == '#': # 강철벽이면 그대로
                                break
                    else: # 그 이외는 이동 및 방향지정
                        chk(com,x,y)
                check = 1 # 다끝나면 반복문 종료시키기 위해 check 1
                break
        if check == 1:
            break
    print(f'#{t+1}',end=" ")
    for i in range(H):
        print(''.join(mapp[i]))

