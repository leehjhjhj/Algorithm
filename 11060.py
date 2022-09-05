import sys

n = int(input())
miro = list(map(int, input().split()))
dp = [1000 for _ in range(n)]
dp[0] = 0

for i in range(n):
    for j in range(1, miro[i]+ 1):
        if i + j < n:
            dp[i + j] = min(dp[i] + 1, dp[i + j])
    print(dp)


if dp[-1] == 1000:
    print(-1)
else:
    print(dp[-1])