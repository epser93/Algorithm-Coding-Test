def paper(N):
    if N == 10:
        return 1
    elif  N == 20:
        return 3
    else:
        return paper(N-10)+paper(N-20)*2

T = int(input())
for t in range(T):
    N = int(input())
    print(f'#{t+1} {paper(N)}')