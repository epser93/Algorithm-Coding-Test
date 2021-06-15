N = int(input())
mapp = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(N):
    col, row = map(int, input().split())
    for j in range(col, col + 10):
        for i in range(99-row, 99-10-row, -1):
            mapp[i][j] += 1
result = 0
for i in range(100):
    for j in range(100):
        if mapp[i][j] >= 1:
            result += 1
print(result)
