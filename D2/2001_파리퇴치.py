T = int(input())
for a in range(T):
    N,M=map(int,input().split())
    arr = []
    max_ = 0
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_ = 0
            for l in range(j,j+M):
                for k in range(i,i+M):
                    sum_ += arr[k][l]
            if sum_ > max_:
                max_ = sum_
    print('#{} {}'.format(a+1,max_))