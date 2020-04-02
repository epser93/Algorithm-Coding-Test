T = int(input())
for k in range(T):
    a,b = map(int,input().split())
    arr = list(map(int,input().split()))
    new_arr = []
    for i in range(a-b+1):
        result = 0
        for j in range(i,i+b):
            result += arr[j]
        new_arr.append(result)
    answer = max(new_arr) - min(new_arr)
    print('#{} {}'.format(k+1, answer))