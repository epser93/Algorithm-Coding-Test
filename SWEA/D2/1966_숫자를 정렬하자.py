T = int(input())
for t in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    result =sorted(arr)
    print(f'#{t+1}', end = " ")
    for i in range(n):
        print(result[i], end =" ")
    print()