# 에라토스테네스의 체
# def solution(n):
#     num=set(range(2,n+1))

#     for i in range(2,n+1):
#         if i in num:
#             num-=set(range(2*i,n+1,i))
#     return len(num)


def isSosu(n):
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            return False
    return True

def solution(n):
    cnt = 0
    for num in range(2, n + 1):
        if isSosu(num):
            cnt += 1
    return cnt

if __name__ == "__main__":
    print(solution(10))
    print(solution(5))