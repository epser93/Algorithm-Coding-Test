T = int(input())
money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for i in range(T):
    result = [0] * 8
    money = int(input())
    for j in range(8):
        if money // money_list[j] > 0:
            result[j] = money // money_list[j]
            money = money % money_list[j]
    print(f'#{i+1}')
    print(* result)