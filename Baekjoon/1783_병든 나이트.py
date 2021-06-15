N, M = map(int, input().split())

if N <= 1:
    print(1)
elif N >= 3:
    if M >= 7:
        print(M - 2)
    elif M >= 4:
        print(4)
    else:
        print(M)
else:
    if M >= 7:
        print(4)
    elif M >= 5:
        print(3)
    elif M >= 3:
        print(2)
    else:
        print(1)