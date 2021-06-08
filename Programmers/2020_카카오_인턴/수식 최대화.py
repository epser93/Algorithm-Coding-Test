from collections import deque

def getPriority(end):
    combList = []
    operators = ["-", "*", "+"]
    
    def generate(idx, end, result):
        if idx == end:
            combList.append(result)
        for i in range(end):
            if operators[i] not in result:
                generate(idx + 1, end, result + [operators[i]])
    
    generate(0, 3, [])
    return combList

def splitOperators(s):
    temp = ''
    result = []
    for string in s:
        if not string.isdecimal():
            result.append(int(''.join(temp)))
            result.append(string)
            temp = ''
            continue
        temp += string
    result.append(int(temp))
    return result

def calculate(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "*":
        return num1 * num2
    elif operator == "-":
        return num1 - num2

def solution(expressions):
    maxNum = float('-inf')
    expressionList = splitOperators(expressions)
    priorities = getPriority(3)
    for priority in priorities:
        operators = deque(priority)
        stack = deque()
        tempExpressionList = deque(expressionList)

        while operators:
            operator = operators.popleft()
            isCalc = False
            for expression in tempExpressionList:
                if isCalc:
                    stack.append(calculate(operator, stack.pop(), expression))
                    isCalc = False
                    continue
                if expression != operator:
                    stack.append(expression)
                else:
                    isCalc = True
            tempExpressionList = stack
            stack = deque()

        if abs(tempExpressionList[0]) > maxNum:
            maxNum = abs(tempExpressionList[0])
    return maxNum

if __name__ == "__main__":
    print(solution("100-200*300-500+20"))
    print(solution("50*6-3*2"))