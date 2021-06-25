N, K = map(int, input().split())
coinSets = [int(input()) for _ in range(N)]
result = 0
for i in range(N-1, -1, -1):
    coin = coinSets[i]
    if K >= coin:
        result += K // coin
        K %= coin
    if K == 0:
        break
print(result)