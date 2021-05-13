def solution(d, budget):
    result = 0
    d = sorted(d)
    for price in d:
        if price > budget:
            break
        budget -= price
        result += 1
    return result


if __name__ == "__main__":
    print(solution([1,3,2,5,4], 9))
    print(solution([2,2,3,3], 10))