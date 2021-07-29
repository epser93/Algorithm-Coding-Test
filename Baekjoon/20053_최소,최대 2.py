import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    minNum, maxNum = float('inf'), float('-inf')
    nums = list(map(int, input().split()))
    for num in nums:
        if num > maxNum:
            maxNum = num
        if num < minNum:
            minNum = num
    print(minNum, maxNum)