def solution(n):
    result = ""
    for num in range(n):
        if num % 2:
            result += "박"
        else:
            result += "수"
    return result

if __name__ == "__main__":
    print(solution(3))
    print(solution(4))