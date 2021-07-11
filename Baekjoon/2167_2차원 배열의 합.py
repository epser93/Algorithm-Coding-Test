import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[x for x in map(int, input().split())] for _ in range(N)]
sumArr = [[0 for _ in range(M+1)] for _ in range(N)]
for i in range(N):
    for j in range(1,M+1):
        sumArr[i][j] = sumArr[i][j-1] + arr[i][j-1]
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    result = 0
    for idx in range(i-1, x):
        result += sumArr[idx][y] - sumArr[idx][j-1]
    print(result)