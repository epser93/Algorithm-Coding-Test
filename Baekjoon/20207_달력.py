N = int(input())
result = 0
calender = [0] * 365
width = 0
height = 0
for _ in range(N):
    start, end = map(int, input().split())
    for i in range(start, end+1):
        calender[i-1] += 1
for day in calender:
    if day == 0:
        result += (width * height)
        width = 0
        height = 0
        continue
    else:
        width += 1
        height = max(height, day)
result += (width * height)
print(result)