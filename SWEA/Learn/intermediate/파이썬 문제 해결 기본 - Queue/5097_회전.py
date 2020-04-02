for t in range(int(input())):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    print('#{} {}'.format(t+1,arr[M%N]))