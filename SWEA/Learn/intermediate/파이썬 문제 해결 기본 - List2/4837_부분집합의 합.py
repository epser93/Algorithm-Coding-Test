T = int(input())
for k in range(T):
    arr = list(map(int,range(1,13)))
    N,K=map(int,input().split())
    n = len(arr)
    count = 0
    for i in range(1<<n):
        new=[]
        for j in range(n):
            if i & (1<<j):
                new.append(arr[j])
        if len(new) == N and sum(new) == K:
            count += 1
    print("#{} {}".format(k+1,count))