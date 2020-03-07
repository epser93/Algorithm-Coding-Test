T = int(input())
for t in range(T):
    N = int(input())
    seq = []
    for a in range(N):
        lis = list(map(int,input().split()))
        seq.append(lis)
    speed = 0
    distance = 0
    for i in range(N):
        if seq[i][0] == 0:
            distance += speed
        elif seq[i][0] == 1:
            speed += seq[i][1]
            distance += speed
        elif seq[i][0] == 2:  
            speed -= seq[i][1]
            if speed <= 0:
                speed = 0
            distance += speed
    print(f'#{t+1} {distance}')