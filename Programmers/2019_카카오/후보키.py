import itertools

def getKeys(relations):
    keys = []
    for i in range(1, len(relations) + 1):
        keys.extend(itertools.combinations(range(len(relations[0])), i))
    return keys

def getUniqueSet(relations, keys):
    keyArr = []
    for key in keys:
        temp = [tuple(relation[idx] for idx in key) for relation in relations]
        if len(set(temp)) == len(relations):
            keyArr.append(key)
    return keyArr

def getDeleteMin(keys):
    result = set(keys)
    for i in range(len(keys) - 1):
        for j in range(i+1, len(keys)):
            if len(set(keys[i]) & set(keys[j])) == len(keys[i]):
                result.discard(keys[j])
    return result

def solution(relation):
    keys = getKeys(relation)
    uniqueKeys = getUniqueSet(relation, keys)
    result = getDeleteMin(relation, uniqueKeys)
    return len(result)

if __name__ == "__main__":
    print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))


