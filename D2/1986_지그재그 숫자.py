T = int(input())
for t in range(T):
    n = int(input())
    sum_ = 0
    for i in range(1,n+1):
        if i % 2 == 1:
            sum_ += i
        else:
            i *= -1
            sum_ += i
    print(f'#{t+1} {sum_}')