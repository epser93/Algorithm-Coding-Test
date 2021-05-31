# 유클리디안 호제법
# def gcdlcm(a, b):
#     c, d = max(a, b), min(a, b)
#     t = 1
#     while t > 0:
#         t = c % d
#         c, d = d, t
#     answer = [c, int(a*b/c)]

#     return answer

def solution(n, m):
    minNum = min(n, m)
    maxNum = max(n, m)
    gongYak = 1
    gongBae = 1
    while 1:
        flag = False
        for num in range(minNum, 1, -1):
            if maxNum % num == 0 and minNum % num == 0:
                gongYak *= num
                maxNum //= num
                minNum //= num
                flag = True
                break
        if flag:
            continue
        gongYak *= 1
        gongBae *= (gongYak * maxNum * minNum)
        break
    return [gongYak, gongBae]

if __name__ == "__main__":
    print(solution(3, 12))
    print(solution(2, 5))