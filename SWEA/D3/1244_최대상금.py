def dfs(idx, numArr):
    global max_money
    if idx == k:
        if int(''.join(numArr)) > max_money:
            max_money = int(''.join(numArr))
        return
    for i in range(0,len(numArr)-1):
        for j in range(i+1,len(numArr)):
            numArr[i], numArr[j] = numArr[j], numArr[i]
            if not visit.get((''.join(numArr), idx)):
                visit[(''.join(numArr), idx)] = 1
                dfs(idx+1, numArr)
            numArr[i], numArr[j] = numArr[j], numArr[i]

for t in range(1, int(input())+1):
    a,b = map(str,input().split())
    num = list(map(str,a))
    k = int(b)
    max_money = -99999999999999993
    visit = {}
    dfs(0,num)
    print('#{} {}'.format(t,max_money))