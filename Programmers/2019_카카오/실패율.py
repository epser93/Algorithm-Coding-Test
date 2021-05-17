def getFailure(challengers, fail):
    return fail / challengers

def solution(N , stages):
    result = []
    answer = []
    challengers = len(stages)
    for i in range(N):
        if challengers == 0:
            result.append([i+1, 0])
            continue
        failPeople = stages.count(i + 1)
        result.append([i+1, getFailure(challengers, failPeople)])
        challengers -= failPeople
    for stage in sorted(result, key= lambda x : x[1], reverse=True):
        answer.append(stage[0])
    return answer

if __name__ == "__main__":
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    print(solution(4, [4,4,4,4]))