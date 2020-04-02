T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    result = max(arr) - min(arr)
    print('#{} {}'.format(i+1,result))