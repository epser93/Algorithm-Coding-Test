def dfs(idx, remain, result, res):
    global answer
    if idx == 4:
        if not visit[result] and remain == 0:
            visit[result] = 1
            answer += 1
        return
    for i in range(N+1):
        if remain - i < 0:
            continue
        dfs(idx+1, remain-i, result+numbers[idx]*i, res + [i])

N = int(input())
numbers = [1, 5, 10, 50]
visit = [0] * 1001
answer = 0
dfs(0, N, 0, [])
print(answer)