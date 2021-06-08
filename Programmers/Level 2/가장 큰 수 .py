# 풀이 1 자릿수 비교
def solution(numbers):
    return str(int(''.join(sorted(list(map(str, numbers)), key=lambda x : x * 4, reverse=True))))

# 풀이 2 Custom Sort
import functools

def comparator(num1, num2):
    if int(num1 + num2) > int(num2 + num1):
        return 1
    elif int(num1 + num2) == int(num2 + num1):
        return 0
    else:
        return -1

def solution(numbers):
    return str(int(''.join(sorted(list(map(str, numbers)), key=functools.cmp_to_key(comparator), reverse=True))))

if __name__ == "__main__":
    print(solution([6, 10, 2]))
    print(solution([3, 30, 34, 5, 9]))
    print(solution([0,0,0,0]))  