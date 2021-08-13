def checkOdd(number):
    cnt = 0
    for num in number:
        if int(num) % 2:
            cnt += 1
    return cnt

def getCnt(number, cnt):
    global maxCnt, minCnt
    cnt += checkOdd(number)
    if len(number) == 1:
        if cnt >= maxCnt:
            maxCnt = cnt
        if cnt <= minCnt:
            minCnt = cnt
        return
    if len(number) == 2:
        num1, num2 = int(number[0]), int(number[1])
        new_number = num1 + num2
        getCnt(str(new_number), cnt)
    if len(number) >= 3:
        for i in range(len(number)-2):
            for j in range(i+1, len(number)-1):
                num1 = int(number[:i+1])
                num2 = int(number[i+1:j+1])
                num3 = int(number[j+1:])
                new_number = num1 + num2 + num3
                getCnt(str(new_number), cnt)


N = input()
maxCnt = float('-inf')
minCnt = float('inf')
getCnt(N, 0)
print(minCnt, maxCnt)