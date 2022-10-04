n, m = tuple(map(int, input().split()))
coin = [int(input()) for _ in range(n)]
cnt = 0

for i in range(n-1, -1, -1):
    if m >= coin[i]:
        while m >= coin[i]:
            m -= coin[i]
            cnt += 1
    if m == 0:
        print(cnt)
        break