n = int(input())
m = int(input())
lst = [ int(input()) for _ in range(m)]
dp = [0] * 100
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, n + 1):
    dp[i] = dp[i-1] + dp[i-2]

if m > 0 :
    chunck = []
    rst = 0
    for i in lst:
        chunck.append(i - rst - 1)
        rst = i
    chunck.append(n - rst)
    answer = 0
    rst2 = 1
    for i in chunck:
        answer = dp[i] * rst2
        rst2 = answer
else:
    answer = dp[n]
print(answer)
