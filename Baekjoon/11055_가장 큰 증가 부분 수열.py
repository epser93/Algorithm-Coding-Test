import sys

input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
dp = [x for x in numbers]
for i in range(1, N):
    for j in range(i-1, -1, -1):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[j] + numbers[i], dp[i])
print(max(dp))