T = int(input())
for t in range(T):
    N = int(input())
    students = [list(map(int,input().split())) for _ in range(N)]
    mapp = [0] * 200
    for start,end in students:
        if start > end:
            start , end = end, start
        for i in range((start-1)//2,(end+1)//2):
            mapp[i] += 1

    print('#{} {}'.format(t+1,max(mapp)))