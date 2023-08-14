board = input()
answer = []
first = 0
second = 0

def check():
    global first
    global second
    length = second - first
    if length % 2 == 1:
        print(-1)
        quit()
    else:
        if length % 4 == 0:
            for _ in range(length):
                answer.append("A")
        else:
            for _ in range(length - 2):
                answer.append("A")
            for _ in range(2):
                answer.append("B")
        first = second
        

for cmd in board:
    if cmd == '.':
        check()
        answer.append(".")
    else:
        second += 1

check()

for aAnswer in answer:
    print(aAnswer, end="")
