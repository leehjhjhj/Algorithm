def solution(word):
    dict = {'A' : 0, 'E' : 1, 'I' : 2, 'O': 3, 'U' : 4} # 알파벳 별 가중치
    word_len = len(word)
    answer = word_len
    for i in range(word_len): 
        temp = 0 
        for j in range(4 - i, -1, -1):
            temp += 5 ** j 
        answer += temp * dict[word[i]]
    return answer
