for t in range(1,int(input())+1):
    A, B = input().split()
    print('#{} {}'.format(t,len(A)+A.count(B)*(1-len(B))))