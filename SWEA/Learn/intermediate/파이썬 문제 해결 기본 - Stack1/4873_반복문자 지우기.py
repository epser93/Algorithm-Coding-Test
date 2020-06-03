T = int(input())
for t in range(T):
    word = input()
    stack = []
    for i in range(len(word)):
        if len(stack) == 0:
            stack.append(word[i])
        else:
            if word[i] != stack[-1]:
                stack.append(word[i])
            else:
                stack.pop()
    print('#{} {}'.format(t+1,len(stack)))