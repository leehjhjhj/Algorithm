n, m = map(int, input().split())
results = []

def print_results():
    for result in results:
        print(result, end=' ')
    print()

def make(curr_num, cnt):
    if curr_num == n + 1:
        if cnt == m:
            print_results()
        return
    
    results.append(curr_num)
    make(curr_num + 1, cnt + 1)
    results.pop()

    make(curr_num + 1, cnt)
    
    return

make(1, 0)
