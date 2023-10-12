import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        if scoville[0] >= K:
            break
            
        if len(scoville) == 1:
            return -1
        
        small = heapq.heappop(scoville)
        smaller = heapq.heappop(scoville)
        
        mixed = small + (smaller * 2)
        
        heapq.heappush(scoville, mixed)
        
        answer += 1
        
    return answer
