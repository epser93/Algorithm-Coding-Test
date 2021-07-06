numbers = list(map(int, input().split()))
num = min(numbers)
while 1:
    cnt = 0
    for i in range(5):
        if not num % numbers[i]:
            cnt += 1
    if cnt >= 3:
        print(num)
        break
    num += 1