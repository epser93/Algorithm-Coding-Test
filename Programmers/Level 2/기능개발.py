from collections import deque
import math
def solution(progresses, speeds):
    progressQueue = deque(progresses)
    speedQueue = deque(speeds)
    result = []
    while progressQueue:
        cnt = 0
        requireDate = math.ceil((100 - progressQueue[0]) / speedQueue[0])
        for idx in range(len(progressQueue)):
            progressQueue[idx] += (speedQueue[idx] * requireDate)
        for progress in progressQueue:
            if progress < 100:
                break
            cnt += 1
        if cnt:
            for _ in range(cnt):
                progressQueue.popleft()
                speedQueue.popleft()
            result.append(cnt)

    return result

if __name__ == "__main__":
    print(solution([93, 30, 55], [1, 30, 5]))
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# a = 3 / 2
# print(math.ceil(a))