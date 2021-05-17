def tenToTwo(num, dim):
    result = ""
    cnt = 0
    while num != 0:
        result = str(num % 2) + result
        num //= 2
        cnt += 1
    if cnt != dim:
        result = ((dim - cnt) * "0") + result
    return result

def decode(bin1, bin2):
    result = ""
    for num1, num2 in zip(bin1, bin2):
        if num1 == "1" or num2 == "1":
            result += "1"
        else:
            result += "0"
    return result

def encoding(decode):
    result = ""
    for elm in decode:
        if elm == "0":
            result += " "
        else:
            result += "#"
    return result

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        map1, map2 = tenToTwo(arr1[i], n), tenToTwo(arr2[i], n)
        decoding = decode(map1, map2)
        answer.append(encoding(decoding))
    return answer

if __name__ == "__main__":
    print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
    print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))