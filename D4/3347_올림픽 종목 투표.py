T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    vote = [0 for _ in range(len(A))]
    for b in B:
        for idx,a in enumerate(A):
            if b >= a:
                vote[idx] += 1
                break
    print('#{} {}'.format(t+1,vote.index(max(vote))+1))