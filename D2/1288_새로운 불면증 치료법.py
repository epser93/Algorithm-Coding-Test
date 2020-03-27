T = int(input())
for t in range(T):
    num = int(input())
    result=[]
    mul = 1
    init = num
    while 1:
        while num != 0:
            if num % 10 not in result:
                result.append(num % 10)
            num //= 10
        if len(result) == 10:
            break
        mul += 1
        num = init * mul
    print(f'#{t+1} {init*mul}')