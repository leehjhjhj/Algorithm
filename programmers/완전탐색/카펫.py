def solution(brown, yellow):
    answer = []
    all = brown + yellow
    for i in range(1, all + 1):
        target = all // i
        if target * i == all:
            if (target - 2) * (i - 2) == yellow:
                answer.append(max(target, i))
                answer.append(min(target, i))
                break
        
    
    return answer
