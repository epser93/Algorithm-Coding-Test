T = int(input())
for i in range(T):
    cnt = [0, 0, 0, 0, 0]
    arr = [2,3,5,7,11]
    num = int(input())
    idx = 0
    for j in arr:
        while num % j == 0:
            num //= j
            cnt[idx] += 1
        idx += 1
    print(f'#{i+1}', end = " ")
    print(*cnt)