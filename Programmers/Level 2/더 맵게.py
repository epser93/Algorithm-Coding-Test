import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for a in scoville:
        heapq.heappush(heap, a)
        
    while 1:
        if len(heap) <= 1:
            answer = -1
            return answer
        first_hot = heapq.heappop(heap)
        second_hot = heapq.heappop(heap)
        mixed = first_hot + second_hot * 2
        heapq.heappush(heap, mixed)
        answer += 1
        if heap[0] > K:  
            return answer