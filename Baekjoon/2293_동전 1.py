n, k = map(int, input().split())
coinSet = [int(input()) for _ in range(n)]
dp = [1] + [0] * k
print(dp)
for coin in coinSet:
    for i in range(coin, k+1):
        dp[i] += dp[i - coin]
    print(dp)
print(dp[k])
