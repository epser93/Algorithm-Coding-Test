T = int(input())
for t in range(T):
    two = list(input())
    three = list(input())
    check = 0 # 이중 for문 탈출 parameter
    for i in range(len(two)*2): # 이진법 0,1 스위칭 되므로 길이 *2 만큼 반복
        copy_two = two[:]
        copy_two[i//2] = str(i % 2) 
        a = ''.join(copy_two)
        for j in range(len(three)*3): # 삼진법 0,1,2 스위칭 길이 *3 만큼 반복
            copy_three = three[:]
            copy_three[j//3] = str(j % 3) 
            b = ''.join(copy_three)
            if int(a,2) == int(b,3):
                print('#{} {}'.format(t+1,int(a,2)))
                check = 1
                break
        if check == 1:
            break