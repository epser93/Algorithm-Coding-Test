N, M = map(int, input().split())
status = list(map(int, input().split()))
for _ in range(M):
    command, command1, command2 = map(int, input().split())
    if command == 1:
        status[command1-1] = command2
    elif command == 2:
        for i in range(command1-1, command2):
            if status[i] == 0:
                status[i] = 1
            else:
                status[i] = 0
    elif command == 3:
        for i in range(command1-1, command2):
            status[i] = 0
    else:
        for i in range(command1-1, command2):
            status[i] = 1
print(*status)