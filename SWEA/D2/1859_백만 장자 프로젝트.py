T = int(input())
for t in range(T):
    N = int(input())
    price = list(map(int,input().split()))
    profit = 0
    max_price = price[-1]
    for i in range(len(price)-2,-1,-1):
        if max_price < price[i]:
            max_price = price[i]
        else:
            profit += (max_price - price[i])
    print('#{} {}'.format(t+1,profit))