import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
for num in sorted(arr):
    print(num)