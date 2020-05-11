T = int(input())
for a in range(T):
    n = int(input())
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    cnt = 2
    arr = [[0 for _ in range(n)] for _ in range(n)]
    x = 0
    y = 0
    i = 0
    arr[0][0] = 1
    for t in range(n*n-1):
        if 0 <= x+dx[i] < n and 0 <= y+dy[i] < n and arr[x+dx[i]][y+dy[i]] == 0:
            arr[x+dx[i]][y+dy[i]] = cnt
        else:
            i+=1
            if i == 4:
                i = 0
            arr[x+dx[i]][y+dy[i]] = cnt
        x+=dx[i]
        y+=dy[i]
        cnt += 1
    print('#{}'.format(a+1))
    for k in range(n):
        print(*arr[k])