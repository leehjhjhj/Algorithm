n = int(input())
picked = set(map(int, input().split()))
m = int(input())
wanna_know = list(map(int, input().split()))

for target in wanna_know:
    if target in picked:
        print(1, end=' ')
    else:
        print(0, end=' ')