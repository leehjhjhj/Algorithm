target = input()

def is_pelin(target):
    if target != target[::-1]:
        return 0
    return 1

print(is_pelin(target))