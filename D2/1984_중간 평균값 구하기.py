T = int(input())
for t in range(T):
    arr = list(map(int,input().split()))
    arr.pop(arr.index(max(arr)))
    arr.pop(arr.index(min(arr)))
    result = round(sum(arr)/len(arr),0)
    print('#{} {}'.format(t+1, int(result)))