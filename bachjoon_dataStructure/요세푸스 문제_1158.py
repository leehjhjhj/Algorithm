from collections import deque

n, k = map(int, input().split())
yose = deque(range(1, n + 1))
results = []
while yose:
    for _ in range(k - 1):
        yose.rotate(-1)
    results.append(yose.popleft())
made = ", ".join(map(str, results))
print(f"<{made}>")