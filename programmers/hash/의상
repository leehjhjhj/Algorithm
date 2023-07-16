from collections import defaultdict

def solution(clothes):
    answer = 1
    dressroom = defaultdict(int)
    for cloth, cloth_type in clothes:
        dressroom[cloth_type] += 1
    
    result = list(dressroom.values())
    for i in result:
        answer *= (i + 1)
    
    
    return answer - 1
