value = input()

stack = []
for v in value:
    if v == "]":
        result = 0
        while stack:
            if stack[-1] == "[":
                stack.pop()
                if result == 0:
                    stack.append(3)
                else:
                    stack.append(3 * result)
                break
            elif stack[-1] == "(":
                print(0)
                exit(0)
            else:
                result += stack.pop()
    elif v == ")":
        result = 0
        while stack:
            if stack[-1] == "(":
                stack.pop()
                if result == 0:
                    stack.append(2)
                else:
                    stack.append(2 * result)
                break
            elif stack[-1] == "[":
                print(0)
                exit(0)
            else:
                result += stack.pop()
    else:
        stack.append(v)

answer = 0
for num in stack:
    if num in ["(", "["]:
        print(0)
        exit(0)
    else:
        answer += num

print(answer)