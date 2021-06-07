def solution(arr1, arr2):
    result = []
    for elm in arr1:
        matrix = []
        for i in range(len(arr2[0])):
            scalar = 0
            for j in range(len(elm)):
                scalar += elm[j] * arr2[j][i]
            matrix.append(scalar)
        result.append(matrix)

    return result

if __name__ == "__main__":
    print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
    print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
    print(solution([[1,2], [4,5], [7,8]], [[1,2,3,4], [5,6,7,8]]))