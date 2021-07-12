N = int(input())
times = list(map(int, input().split()))
times.sort()
dp = [times[0]] + [0] * (N-1)
for i in range(1, N):
    dp[i] = dp[i-1] + times[i]
print(sum(dp))