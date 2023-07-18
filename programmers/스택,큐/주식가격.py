def solution(prices):
    stack = []
    answer = [0 for _ in range(len(prices))]

    for i in range(len(prices)):
        if i == 0:
            stack.append(i)
            continue

        while stack and prices[i] < prices[stack[-1]]:
            index = stack.pop()
            answer[index] = i - index

        stack.append(i)

    for i in range(len(prices)):
        if answer[i] == 0:
            answer[i] = len(prices) - 1 - i

    return answer
