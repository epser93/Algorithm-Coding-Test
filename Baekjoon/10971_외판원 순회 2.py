def perm(idx,select):
    global min_cost
    if idx == N:
        if cost[select[-1]-1][select[0]-1] != 0:
            select += [select[0]]
        else:
            return
        result = 0
        for j in range(N):
            result += cost[select[j]-1][select[j+1]-1]
        if result < min_cost:
            min_cost = result
    for i in range(1,N+1):
        if i not in select:
            if select and cost[select[-1]-1][i-1] != 0:
                perm(idx+1, select + [i])
            elif not select:
                perm(idx+1, select + [i])

N = int(input())
cost = list(list(map(int,input().split())) for _ in range(N))
min_cost = 9999999999
perm(0,[])
print(min_cost)