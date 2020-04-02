T = int(input())
for t in range(T):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int,input())))
    sum_ = 0
    for i in range(N // 2):
        for j in range(N//2-i,N//2+1+i):
            sum_ += board[i][j]

    sum_ += sum(board[N//2])

    for x in range(N//2+1,N):
        for y in range(x-N//2,N+N//2-x):
            sum_ += board[x][y]

    print(f'#{t+1} {sum_}')