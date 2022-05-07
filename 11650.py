n = int(input())
a = []
for _ in range(n):
    x = tuple(map(int, input().split()))
    a.append(x)

a.sort(key=lambda x: (x[0], x[1]))
print(a)
for x, y in a:
    print(x, y)