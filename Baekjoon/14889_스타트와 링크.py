def dfs(index,selectA,before):
    global min_point
    if index == n // 2:
        selectB = [c for c in range(n)]
        result_a , result_b = 0, 0
        for j in selectA:
            selectB.remove(j)
        for a in range(n // 2):
            for b in range(a, n//2):
                result_a += score_map[selectA[a]][selectA[b]] + score_map[selectA[b]][selectA[a]]
                result_b += score_map[selectB[a]][selectB[b]] + score_map[selectB[b]][selectB[a]]
        if abs(result_a - result_b) <= min_point:
            min_point = abs(result_a - result_b)
        return
    for i in range(before,n):
        dfs(index+1,selectA+[i],i+1)

n = int(input())
score_map = [list(map(int,input().split())) for _ in range(n)]
min_point = 9999999999999
dfs(0,[],0)
print(min_point)