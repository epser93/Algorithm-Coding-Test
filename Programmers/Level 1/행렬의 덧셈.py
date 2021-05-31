def solution(arr1, arr2):
    result = []
    for tempArr1, tempArr2 in zip(arr1, arr2):
        temp = []
        for elm1, elm2 in zip(tempArr1, tempArr2):
            temp.append(elm1 + elm2)
        result.append(temp)
    return result

if __name__ == "__main__":
    print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
    print(solution([[1],[2]], [[3],[4]]))