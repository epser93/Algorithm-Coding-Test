for t in range(10):
    n = int(input())
    arr = []
    cnt = 0
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    for y in range(n):
        check = 0
        for x in range(n):
            if arr[x][y] == 1:
                check = 1
            if arr[x][y] == 2 and check == 1:
                cnt += 1
                check = 0
    print('#{} {}'.format(t+1,cnt))