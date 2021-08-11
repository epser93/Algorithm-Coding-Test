N, M = map(int, input().split())
trains = [[0 for _ in range(20)] for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(M)]
enterDict = {}
cnt = 0
for command in commands:
    if command[0] == 1:
        trains[command[1]-1][command[2]-1] = 1
    elif command[0] == 2:
        trains[command[1]-1][command[2]-1] = 0
    elif command[0] == 3:
        prev = trains[command[1]-1][0]
        trains[command[1]-1][0] = 0
        for i in range(1, 20):
            trains[command[1]-1][i], prev = prev, trains[command[1]-1][i]
    else:
        prev = trains[command[1]-1][-1]
        trains[command[1]-1][-1] = 0
        for i in range(18, -1, -1):
            trains[command[1]-1][i], prev = prev, trains[command[1]-1][i]

for train in trains:
    train = tuple(train)
    if not enterDict.get(train):
        cnt += 1
        enterDict[train] = 1
print(cnt)