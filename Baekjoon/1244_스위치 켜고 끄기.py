def turn(idx):
    if switch[idx] == 0:
        switch[idx] = 1
    else:
        switch[idx] = 0

n = int(input())
switch = list(map(int, input().split()))
sequences = []
for _ in range(int(input())):
    sequences.append(list(map(int, input().split())))

for sequence in sequences:
    sex, num = sequence[0], sequence[1]
    if sex == 1:
        for i in range(n):
            if (i+1) % num == 0:
                turn(i)
    else:
        cnt = 0
        num-=1
        while 1:
            if 0 > num-cnt or num-cnt >= n or 0 > num+cnt or num+cnt >= n or switch[num-cnt] != switch[num+cnt]:
                startIdx, endIdx = num-(cnt-1), num+(cnt-1) 
                break
            cnt += 1
        if startIdx == endIdx:
            turn(startIdx)
        else:
            for i in range(startIdx, endIdx+1):
                turn(i)
for i in range(0, n, 20):
    print(*switch[i:i+20])