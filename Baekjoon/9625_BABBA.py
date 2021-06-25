K = int(input())
result = [0,0]
for i in range(K):
    if i == 0:
        result[1] = 1
        continue
    bCnt = result[0] + result[1]
    result[0] = result[1]
    result[1] = bCnt
print(*result)