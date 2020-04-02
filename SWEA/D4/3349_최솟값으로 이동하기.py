T = int(input())
for t in range(T):
    W, H, N = map(int,input().split())
    way = [list(map(int,input().split())) for _ in range(N)]
    X, Y = way[0][0], way[0][1]
    result = 0
    for x,y in way:
        if (X > x and Y < y) or (X < x and Y > y): # x나 y값 둘 중 하나만 크면 대각선 이용 불가
            result += (abs(X-x) + abs(Y-y)) 
        else: # min(abs(X-x),abs(Y-y))만큼 대각선 사용 + 나머지 가로,세로방향거리
            result += (min(abs(X-x),abs(Y-y)) + abs(abs(X-x)-abs(Y-y)))
        X,Y = x,y # 현 위치 변경
    print('#{} {}'.format(t+1,result))