sequences = list(map(int, input().split()))

while 1:
    for i in range(4):
        if sequences[i] > sequences[i+1]:
            sequences[i], sequences[i+1] = sequences[i+1], sequences[i]
            print(*sequences)
            if sequences == [1,2,3,4,5]:
                exit(0)