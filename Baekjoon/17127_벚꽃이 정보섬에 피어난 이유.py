import sys

def multiply(arr):
    point = 1
    for elm in arr:
        point *= elm
    return point

input = sys.stdin.readline

N = int(input())
flowers = list(map(int, input().split()))
maxP = float('-inf')
for i in range(N - 3):
    for j in range(i + 1, N - 2):
        for z in range(j + 1, N - 1):
            for k in range(z + 1, N):
                p = multiply(flowers[:i+1]) + multiply(flowers[i+1:j+1]) + multiply(flowers[j+1:z+1]) + multiply(flowers[z+1:k+1])
                if p > maxP:
                    maxP = p

print(maxP)


            