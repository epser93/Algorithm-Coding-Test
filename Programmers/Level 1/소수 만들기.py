def isDecimal(num):
    if num == 1:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def setIdx(length, prevIdx, deep, visit):
    if deep == 3:
        combIdx.append(visit)
        return 
    for i in range(prevIdx, length):
        if i not in visit:
            setIdx(length, i, deep + 1, visit + [i])

def solution(nums):
    global combIdx
    combIdx = []
    result = 0
    setIdx(len(nums), 0, 0, [])
    for idx in combIdx:
        num = nums[idx[0]] + nums[idx[1]] + nums[idx[2]]
        if isDecimal(num):
            result += 1
    return result

if __name__ == "__main__":
    print(solution([1,2,3,4]))
    print(solution([1,2,7,6,4]))