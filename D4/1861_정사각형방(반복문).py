def iswall(x,y): # 벽 체크 맵의 범위안에 있는지 + 다음칸과의 차가 1인지
    if (0 <= x < n) and (0 <= y < n) and (arr[x][y] - arr[x-dx[i]][y-dy[i]] == 1):
        return False
    return True 

T = int(input())
for t in range(T):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    max_cnt = 0 # 결과값 / 이동한 방의 최대 개수가 저장될 변수
    room = 9999999 # 결과값 2 / 시작 방번호가 저장될 변수
    for x in range(n): # 모든 x,y 탐색
        for y in range(n):
            init_x = x # x와 y가 탐색을 하며 변동 되므로 최초 위치를 따로 저장함. 나중에 cnt와 room 비교를 위해 필요함
            init_y = y
            cnt = 1
            idx = 0 # for문 돈 횟수 
            i = 0
            while 1:
                if idx > 4: # 현재 위치에서 4방향을 다 돌고도 갈 곳이 없다면 종료
                    break
                if iswall(x+dx[i],y+dy[i]) == False: 
                    x+=dx[i]
                    y+=dy[i]
                    cnt += 1
                    idx = 0 # 벽체크 후 갈 수 있다면 한칸 간 후 다시 4방향 체크를 할 것이기에 0으로 초기화
                    i = 0
                else:
                    i += 1 
                    idx += 1
                if i == 4:
                    i = 0
            if cnt > max_cnt:
                max_cnt = cnt
                room = arr[init_x][init_y]
            elif cnt == max_cnt:
                if room > arr[init_x][init_y]:
                    room = arr[init_x][init_y]
    print('#{} {} {}'.format(t+1,room,max_cnt))
            