# 첫번째 풀이

def solution(phone_book):
    phone_set = set(phone_book)
    
    for number in phone_book:
        prefix = ""
        for digit in number:
            prefix += digit
            if prefix in phone_set and prefix != number:
                return False
    
    return True

# 두번째 풀이
def solution(phone_book):
    hash_map = {}
    
    # 해시 맵에 전화번호를 키로 저장
    for number in phone_book:
        hash_map[number] = 1
    
    # 전화번호부를 순회하며 접두어 여부를 확인
    for number in phone_book:
        prefix = ""
        for digit in number:
            prefix += digit
            if prefix in hash_map and prefix != number:
                return False
    
    return True

# 세번째 풀이
def solution(phone_book):
    phone_book.sort()  
    
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return True

