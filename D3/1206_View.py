for j in range(10):
    n= int(input())
    lis = list(map(int,input().split()))

    count = 0

    for i in range(2,len(lis)-2):
        check_1 = lis[i] - lis[i-2]
        check_2 = lis[i] - lis[i-1]
        check_3 = lis[i] - lis[i+1]
        check_4 = lis[i] - lis[i+2]
        if check_1 > 0 and check_2 > 0 and check_3 > 0 and check_4 > 0:
            count += min(check_1,check_2,check_3,check_4)
    print(f"#{j+1 }",count)