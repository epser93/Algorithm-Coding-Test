N = int(input())
def perm(idx,select):
    if idx == N:
        print(*select)
    for i in range(1, N+1):
        if i not in select:
            perm(idx+1, select+[i])
perm(0,[])