from collections import deque

def solution(priorities, location):
    queue = deque()
    cnt = 0
    for idx, priority in enumerate(priorities):
        queue.append((idx, priority))
    while queue:
        maxNum = max(queue, key=lambda x: x[1])[1]
        q = queue.popleft()
        if q[1] < maxNum:
            queue.append(q)
            continue
        cnt += 1
        if q[0] == location:
            return cnt



if __name__ == "__main__":
    print(solution([2, 1, 3, 2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 0))