# def solution(arr):
#     minIdx = arr.index(min(arr))
#     arr.pop(minIdx)
#     if arr[-1:] == []:
#         return [-1]
#     return arr

def solution(arr):
    arr = [i for i in arr if i > min(arr)]
    if arr[-1:] == []:
        return [-1]
    return arr

if __name__ == "__main__":
    print(solution([4,3,2,1]))
    print(solution([10]))