import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
stack = deque([])
current = []
result = 0

for i in range(N):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        if current != []:
            stack.append(current)
        temp[2] -= 1
        current = temp[1:3]
    else:
        if current == []:
            continue
        current[1] -= 1

    if current[1] == 0:
        result += current[0]
        if len(stack):
            current = stack.pop()
        else:
            current = []

print(result)
