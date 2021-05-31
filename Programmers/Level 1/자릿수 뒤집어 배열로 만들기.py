def solution(n):
    result = []
    while n != 0:
        result.append(n % 10)
        n //= 10
    return result

if __name__ == "__main__":
    print(solution(12345))

# print(12345 % 10)