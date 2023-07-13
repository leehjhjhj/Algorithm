def solution(targets):
    targets.sort(key=lambda x: x[1])  
    target_j = float('inf')
    answer = 0
    
    for i, j in targets:
        if i >= target_j:
            answer += 1
            target_j = j
        target_j = min(target_j, j)

    return answer + 1
