def validationYaksu(num):
    cnt = 0
    for i in range(1,num + 1):
        if num % i == 0:
            cnt += 1
    if cnt % 2:
        return True
    return False

def solution(left, right):
    result = 0
    for num in range(left, right + 1):
        if validationYaksu(num):
            result -= num
        else:
            result += num
    return result

if __name__ == "__main__":
    print(solution(13, 17))
    print(solution(24, 27))