def solution(arr):
    result = []
    prev = -1
    for i in range(len(arr)):
        if arr[i] == prev:
            continue
        prev = arr[i]
        result.append(arr[i])

if __name__ == "__main__":
    print(solution([1,1,3,3,0,1,1]))
    print(solution([4,4,4,3,3]))