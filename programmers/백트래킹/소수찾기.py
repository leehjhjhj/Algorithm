def solution(numbers):
    n = len(numbers)
    result = []
    unique_numbers = set() 
    used = [False] * n

    def check(target):
        if len(target) == 0 or target[0] == "0":
            return False
        
        prefix = "".join(target)
        prefix = int(prefix)

        if prefix < 2:
            return False

        for i in range(2, prefix):
            if prefix % i == 0:
                return False
        return True

    def make(curr_num):
        if check(result):
            unique_numbers.add(int("".join(result)))

        if curr_num == n:
            return

        for i in range(n):
            if used[i]:
                continue
            result.append(numbers[i])
            used[i] = True
            make(curr_num + 1)
            used[i] = False
            result.pop()
	
    make(0)
    return len(unique_numbers)
