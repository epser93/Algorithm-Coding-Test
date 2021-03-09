import sys

input = sys.stdin.readline

T = int(input())
times = [int(input()) for x in range(T)]

for time in times:
    rangeNum = int(time ** 0.5)
    for num in range(rangeNum, -1, -1):
        if num + num ** 2 <= time:
            print(num)
            break