def score(a):
    cnt = 0
    cnt_array = []
    for OX in a:
        if OX == 'O':
            cnt += 1
        else:
            cnt_array.append(cnt)
            cnt = 0
    cnt_array.append(cnt)
    
    score = 0
    for i in cnt_array:
        if i == 0:
            pass
        elif i == 1:
            score += 1    
        else:
            sum = 0
            for j in range(1, i + 1):
                sum = sum + j
            score += sum
    return score
n = int(input())

array_= [
    list(input())
    for _ in range(n) 
]
for i in array_:
    print(score(i))