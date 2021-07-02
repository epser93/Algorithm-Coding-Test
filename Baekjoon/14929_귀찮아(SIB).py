n = int(input())
xi = list(map(int, input().split()))
sumArr = [xi[0]] * n
for i in range(1, n):
    sumArr[i] = sumArr[i-1] + xi[i]
result = 0
for i in range(n-1):
    result += xi[i]*(sumArr[-1] - sumArr[i])
print(result)