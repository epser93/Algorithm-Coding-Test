# def solution(n):
#     n **= 0.5
#     if str(n)[-1] != '0':
#         return -1
#     return int((n + 1) ** 2)

def solution(n):
    n **= 0.5
    if n % 1 == 0:
        return int((n + 1) ** 2)
    return -1

if __name__ == "__main__":
    print(solution(121))
    print(solution(3))
