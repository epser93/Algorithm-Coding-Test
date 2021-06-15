N, M = map(int, input().split())
result = 0
mapp = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(N):
    postions = list(map(int, input().split()))
    for i in range(postions[0], postions[2] + 1):
        for j in range(postions[1], postions[3] + 1):
            mapp[i - 1][j - 1] += 1

for i in range(100):
    for j in range(100):
        if mapp[i][j] > M:
            result += 1

print(result)
