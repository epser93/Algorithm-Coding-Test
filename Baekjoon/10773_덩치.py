from collections import deque
stack = deque()
result = 0
for _ in range(int(input())):
    num = int(input())
    if num != 0:
        stack.append(num)
        result += num
    else:
        result -= stack.pop()
print(result)