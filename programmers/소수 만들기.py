def is_sosu(target):
    for i in range(2, target):
        if target % i == 0:
            return False
    return True
    

def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if is_sosu(nums[i]+nums[j]+nums[k]):
                    answer += 1
    return answer
