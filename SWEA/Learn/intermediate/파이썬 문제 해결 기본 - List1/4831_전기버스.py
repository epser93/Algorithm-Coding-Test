T = int(input())
for i in range(T):
    K, N, M = map(int,input().split())
    location = list(map(int,input().split()))
    idx = K
    count = 0
    last = 0
    while idx < N:
        if idx == 0 or idx == last:
            count = 0
            break

        if idx in location:
            last = idx
            count += 1
            idx += K
        else:
            idx -= 1

    print('#{} {}'.format(i+1,count))