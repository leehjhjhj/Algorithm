def solution(prices):
    stack = []
    answer = [i for i in range(len(prices) - 1, -1, -1)]

    for i in range(len(prices)):
        if i == 0:
            stack.append(i)
            continue

        while stack and prices[i] < prices[stack[-1]]:
            index = stack.pop()
            answer[index] = i - index

        stack.append(i)
    
    return answer

