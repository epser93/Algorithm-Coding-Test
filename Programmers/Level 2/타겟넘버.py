
cnt = 0

def comb(idx, numbers, target, result):
    global cnt
    if idx == len(numbers):
        if result == target:
            cnt += 1
        return
    for i in range(1,3):
        comb(idx+1, numbers, target, result+numbers[idx]*(-1)**i)

def solution(numbers, target):
    global cnt
    comb(0, numbers, target, 0)
    return cnt


if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3))