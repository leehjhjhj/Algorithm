n, m = map(int,input().split())
arr = list(map(int, input().split()))

left, right = 0, 1
answer = 0
while right <= n and left <= right:
    total = sum(arr[left:right])

    if total == m:
        answer += 1
        
        right += 1

    elif total > m:
        left += 1

    else:
        right += 1
print(answer)

