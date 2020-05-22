T = int(input())
for t in range(T):
    str1 = input()
    str2 = input()
    for i in range(len(str2)-len(str1)+1):
        check = 0
        for j in range(len(str1)):
            if str1[j] != str2[i+j]:
                break
            else:
                check += 1
        if check == len(str1):
            print('#{} {}'.format(t+1, 1))
            break
    else:
        print('#{} {}'.format(t+1, 0))