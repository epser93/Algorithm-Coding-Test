pw = {
    '0001101' : '0',
    '0011001' : '1',
    '0010011' : '2',
    '0111101' : '3',
    '0100011' : '4',
    '0110001' : '5',
    '0101111' : '6',
    '0111011' : '7',
    '0110111' : '8',
    '0001011' : '9'
}

for t in range(1, int(input())+1):
    sero , garo = map(int,input().split())
    case = list(input() for _ in range(sero))

    temp_pw = ''
    for temp in case:
        if '1' in temp:
            for i in range(garo-1,-1,-1):
                if temp[i] == '1':
                    break
            for j in range(i-56+1,i+1,+7):
                temp_pw += pw[temp[j:j+7]]
            break
    temp_ans = 0
    for i in range(len(temp_pw)):
        num = int(temp_pw[i])
        if i % 2 == 0:
            temp_ans += 3*num
        else:
            temp_ans += num

    if temp_ans % 10 == 0:
        result = 0
        for a in temp_pw:
            result += int(a)
        print('#{} {}'.format(t,result))
    else:
        print('#{} {}'.format(t,0))
