def solution(array, commands):
    answer = []
    for command in commands:
        result = []
        for num in range(command[0]-1,command[1]):
            result.append(array[num])
        print(result)
        result.sort()
        answer.append(result[command[2]-1])
    return answer