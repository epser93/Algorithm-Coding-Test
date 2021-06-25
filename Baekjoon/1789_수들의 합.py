S = int(input())
num = 0
i = 1
cnt = 0
while 1:
    num += i
    if num > S:
        break
    cnt += 1
    i += 1
print(cnt)