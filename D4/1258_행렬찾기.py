def search(row, col):
    global X
    global Y
    dx = [0, 0, 1]  # 우 좌 하
    dy = [1, -1, 0]
    mapp[row][col] = 0 # 다녀간곳은 0으로 바꿔줌 왔던 곳 중복으로 방문하는 것을 방지하기 위함
    for i in range(3):
        if 0 <= row+dx[i] < n and 0 <= col+dy[i] < n and mapp[row+dx[i]][col+dy[i]] != 0: 
            if row+dx[i] - init_x + 1 >= X: # 길이가 최대인 부분이 행렬의 세로 길이
                X = row+dx[i] - init_x + 1
            if col+dy[i] - init_y >= Y: # 길이가 최대인 부분이 행렬의 가로 길이
                Y = col+dy[i] - init_y + 1
            search(row+dx[i], col+dy[i])
    return X, Y

T = int(input())
for t in range(T):
    n = int(input())
    mapp = []
    cnt = 0 # 행렬 개수 카운팅
    result = []
    for _ in range(n):
        mapp.append(list(map(int, input().split())))

    for y in range(n):
        for x in range(n):
            if mapp[x][y] != 0: # 0이 아닌 부분이 있으면 탐색 시작할꺼임
                cnt += 1 
                X = 0 # 결과값에 들어갈 행
                Y = 0 # 결과값에 들어갈 열
                init_x = x # 최초행
                init_y = y # 최초열
                result.append(search(x, y))
    sorted_result = sorted(result,key= lambda x: (x[0]*x[1],x[0]))
    print(f'#{t+1}',cnt, end =" ")
    for i in range(len(sorted_result)):
        print(*sorted_result[i],end =" ")
    print()