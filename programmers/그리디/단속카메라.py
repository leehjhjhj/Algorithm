def solution(routes):
    routes.sort(key=lambda x: x[0])
    answer = 0
    m = 30000
    for i, j in routes:
        if i > m:
            answer += 1
            m = j
        m = min(m, j)
        
    return answer + 1
