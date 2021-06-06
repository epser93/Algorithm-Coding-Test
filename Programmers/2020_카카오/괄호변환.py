from collections import deque

def splitBracket(p):
    num1 = 0
    num2 = 0
    for idx, bracket in enumerate(p):
        if bracket == "(":
            num1 += 1
        else:
            num2 += 1
        if num1 == num2:
            return p[:idx+1], p[idx+1:]

def makeCompletedBrackets(u, uu):
    result = "("
    result += uu + ")"
    u = u[1:-1]
    for elm in u:
        if elm == "(":
            result += ")"
        else:
            result += "("
    return result

def check(u):
    if u[0] == ")":
        return False
    stack = deque()
    for elm in u:
        if not stack:
            stack.append(elm)
            continue
        if elm == "(":
            stack.append(elm)
        else:
            stack.pop()
    if stack:
        return False
    return True

def makeResult(w):
    if w == "":
        return ""
    u, v = splitBracket(w)
    if check(u):
        return u + makeResult(v)
    return makeCompletedBrackets(u, makeResult(v))

def solution(p):
    if p == "":
        return ""
    return makeResult(p)

if __name__ == "__main__":
    print(solution("(()())()"))
    print(solution(")("))
    print(solution("()))((()"))