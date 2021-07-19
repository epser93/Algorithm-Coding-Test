n, m = map(int, input().split())
denominator = 1
numerator = 1
for _ in range(m):
    numerator *= n
    n -= 1
for i in range(1,m+1):
    denominator *= i
print(numerator // denominator)