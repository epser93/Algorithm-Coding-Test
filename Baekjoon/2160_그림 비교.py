def calculate(drawing1, drawing2):
    cnt = 0
    for i in range(5):
        for j in range(7):
            if drawing1[i][j] != drawing2[i][j]:
                cnt += 1
    return cnt

N = int(input())
drawings = [[list(input()) for _ in range(5)] for _ in range(N)]
result = None
minCnt = float('inf')
for i in range(N-1):
    for j in range(i+1, N):
        tempCnt = calculate(drawings[i], drawings[j])
        if tempCnt < minCnt:
            minCnt = tempCnt
            result = (i+1, j+1)
print(*result)
