def dfs(start, result, resultLen):
    global maxNum, visit
    if resultLen == maxNum:
        print(*result)
        exit(0)
    for i in range(start, start+2):
        num = int(N[start:i+1]) 
        if 1<= num <= maxNum and not visit[num]:
            visit[num] = 1
            dfs(i+1, result+[num], resultLen+1)
            visit[num] = 0

N = input()
nLength = len(N)
if nLength > 9:
    maxNum = 9 + (nLength-9)//2
else:
    maxNum = nLength
visit = [0] * (maxNum + 1)
dfs(0,[],0)