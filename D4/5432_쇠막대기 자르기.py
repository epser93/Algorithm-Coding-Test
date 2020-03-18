T= int(input())
for t in range(T):
    mapp=input()
    stack = []
    result = 0
    for i in range(len(mapp)):
        if len(stack) == 0: # stack 비었는지 체크
            stack.append(mapp[i])
        else: 
            if mapp[i] == ")": # )를 만나면
                if mapp[i-1] == "(": # 바로 앞이 ( 라면 레이져 성립
                    stack.pop()
                    result += len(stack)
                else: # 바로 앞이 ( 아니면 레이져가 아니며 앞에 레이저로 혼자 떨어져 나온 막대 계산
                    stack.pop()
                    result += 1
            else: # ( 이면 stack에 push
                stack.append(mapp[i])
    print('#{} {}'.format(t+1,result))