def calculate(num1, num2, oper):
    if oper == 0:
        return num1 + num2
    elif oper == 1:
        return num1 - num2
    elif oper == 2:
        return num1 * num2
    else:
        if num1 < 0:
            return ((num1 * -1) // num2) * -1
        return num1 // num2

def dfs(idx, end, result):
    global operators, numbers, maxNum, minNum
    if idx == end:
        if result >= maxNum:
            maxNum = result
        if result <= minNum:
            minNum = result
        return
    for i in range(4):
        if operators[i]:
            operators[i] -= 1
            dfs(idx+1, end, calculate(result, numbers[idx], i))
            operators[i] += 1

N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
maxNum = float('-inf')
minNum = float('inf')
dfs(1, len(numbers), numbers[0])
print(maxNum)
print(minNum)