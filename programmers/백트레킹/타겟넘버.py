def solution(numbers, target):
    answer = 0
    
    def make(sum_, index):
        nonlocal answer
        
        if index == len(numbers):
            if sum_ == target:
                answer += 1
            return
        
        make(sum_ + numbers[index], index + 1)
        make(sum_ - numbers[index], index + 1)

    make(0, 0)
    return answer
