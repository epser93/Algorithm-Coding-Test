t = int(input())
for a in range(t):
    n = int(input())
    lis = [[0 for i in range(n)] for j in range(n)]
    for x in range(n):
        lis[x][0] = 1
        for y in range(1,n):
            if x == 0:
                lis[x][y] = 0
            else:
                lis[x][y] = lis[x-1][y-1] + lis[x-1][y]
    print("#{}".format(a+1))
    for k in range(n):
        print(* lis[k][0:k+1])