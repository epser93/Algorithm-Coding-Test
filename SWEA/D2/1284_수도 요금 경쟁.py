T = int(input())
for t in range(T):
    arr = list(map(int,input().split()))
    fee_A = arr[0] * arr[4]
    if arr[4] <= arr[2]:
        fee_B = arr[1]
    else:
        fee_B = arr[1] + arr[3] * (arr[4]-arr[2]) 
    if fee_A > fee_B:
        print(f'#{t+1} {fee_B}')
    else:
        print(f'#{t+1} {fee_A}')