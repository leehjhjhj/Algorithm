n = int(input())
schedule = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
dp = [0] * n

for i in range(n):
    if i == 0:
        if schedule[0][0] == 1:
            dp[0] = schedule[0][1]
        else:
            dp[0] = 0
    elif i == 1:
        if schedule[1][0] == 1:
            if schedule[0][0] == 2:
                dp[1] = schedule[0][1] + schedule[1][1]
            else:
                dp[1] = schedule[1][1]
        else:
            dp[1] = 0
    else:
        dp[i] = 
