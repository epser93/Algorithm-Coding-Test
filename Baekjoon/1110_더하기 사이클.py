startNum = input()
num = startNum
cnt = 0
while 1:
    if len(num) < 2:
        num = num[-1] + num[-1]
    else:
        num = num[-1] + str(int(num[0]) + int(num[1]))[-1]
    cnt += 1
    if int(num) == int(startNum):
        break
print(cnt)