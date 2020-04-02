N = int(input())
tsn = ['3','6','9']
for i in range(1,N+1):
    if len(str(i)) > 1:
        check = 0
        for j in range(len(str(i))):
            if str(i)[j:j+1] in tsn:
                check += 1
        if check > 0:
            print('-'*check,end=" ")
        else:
            print(i, end = " ")
    else:
        if i % 3 == 0:
            print("-",end = " ")
        else:
            print(i,end = " ")