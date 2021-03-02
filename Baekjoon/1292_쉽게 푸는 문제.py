A, B = map(int, input().split())

sumList = [0, 1]
num = 2
cnt = 1
flag = False
while 1:
    if flag == True:
        break
    for i in range(num):
        if cnt == B:
            flag = True
            break
        sumList.append(sumList[-1] + num)
        cnt += 1
    num += 1
print(sumList[B] - sumList[A - 1])