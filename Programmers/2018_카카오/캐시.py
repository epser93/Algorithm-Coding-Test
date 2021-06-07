from collections import deque

def solution(cacheSize, cites):
    cache = deque(maxlen=cacheSize)
    time = 0
    for city in cites:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            cache.append(city)
            time += 5

    return time

if __name__ == "__main__":
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
    print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
    print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
    print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
    print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))