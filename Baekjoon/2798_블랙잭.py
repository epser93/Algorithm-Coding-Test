def dfs(idx, prev, result):
    global answer
    if idx == 3:
        if answer[1] > M - result >= 0:
            answer[0] = result
            answer[1] = M - result
        return
    for i in range(prev, len(cards)):
        dfs(idx+1, i+1, result + cards[i])

N, M = map(int, input().split())
cards = list(map(int, input().split()))
answer = [float('inf'), M] # 정답, 차이
dfs(0,0,0)
print(answer[0])