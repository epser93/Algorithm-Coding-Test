T = int(input())
moderator = ['*','-','+','/']
for t in range(T):
    arr = list(input().split())
    stack = []
    for i in arr:
        if i =='.' and len(stack) == 1:
            print('#{} {}'.format(t+1,*stack))
            break
        elif i == '.' and len(stack) != 1:
            print('#{} {}'.format(t+1,'error'))
            
        if i not in moderator:
            stack.append(i)
        else:
            if len(stack) < 2:
                print('#{} {}'.format(t+1,'error'))
                break
            elif i == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b)*int(a))
            elif i == '/':
                a = stack.pop()
                b = stack.pop()
                result = int(int(b)/int(a))
                stack.append(result)
            elif i == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b)+int(a))
            elif i == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b)-int(a))            