def solution(numbers):
    result = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            num = numbers[i] + numbers[j]
            if num not in result:
                result.append(num)
    return sorted(result)

if __name__ == "__main__":
    print(solution([2,1,3,4,1]))
    print(solution([5,0,2,7]))