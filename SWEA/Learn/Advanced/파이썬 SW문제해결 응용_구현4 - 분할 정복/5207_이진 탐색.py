def search(value, start, end, dir):
    while start <= end:
        center = (start + end) // 2
        if value == arrA[center]:
            return 1
        elif value < arrA[center]:
            end = center -1
            if dir == -1:
                return 0
            dir = -1
        elif value > arrA[center]:
            start = center + 1
            if dir == 1:
                return 0
            dir = 1
    return 0

for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    arrA = sorted(list(map(int,input().split())))
    arrB = list(map(int,input().split()))
    cnt = 0

    for i in range(M):
        cnt += search(arrB[i],0,N-1,0)
        
    print('#{} {}'.format(t,cnt))