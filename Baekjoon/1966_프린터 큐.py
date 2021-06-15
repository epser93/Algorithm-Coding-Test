from collections import deque

for _ in range(int(input())):
    cnt = 0
    n, targetIdx = map(int, input().split())
    priorities = list(map(int, input().split()))
    queue = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    priorities.sort() 
    while queue:
        prior, documentIdx = queue.popleft()
        if prior == priorities[-1]:
            priorities.pop()
            cnt += 1
            if documentIdx == targetIdx:
                print(cnt)
                break
        else:
            queue.append((prior, documentIdx))