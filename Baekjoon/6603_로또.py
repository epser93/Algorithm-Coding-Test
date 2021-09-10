def dfs(idx, nextIdx, result):
    if idx == 6:
        print(*result)
        return
    for i in range(nextIdx, len(lottoNumbers)):
        dfs(idx+1, i+1, result+[lottoNumbers[i]])

try:
    while 1:
        inputNumbers = list(map(int, input().split()))
        N, lottoNumbers = inputNumbers[0], inputNumbers[1:]
        dfs(0, 0, [])
        print()
except:
    exit()