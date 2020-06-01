T = int(input())
for t in range(T):
    word = input()
    stack = [0]
    for i in range(len(word)):
        if word[i] != '}' and word[i] !=')' and word[i] !='(' and word[i] !='{':
            continue
        if word[i] == "}":
            if stack[-1] == "{":
                stack.pop()
            else:
                stack.append(word[i])
                break
        if word[i] == ")":
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(word[i])
                break
        elif word[i] == '{' or word[i] =='(':
            stack.append(word[i])
    if len(stack) > 1:
        print(f'#{t+1} {0}')
    else:
        print(f'#{t+1} {1}')