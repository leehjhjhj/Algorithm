n, m = map(int, input().split())
results = []

def print_results():
    for result in results:
        print(result, end=' ')
    print()

def make(curr_num):
    if curr_num == m + 1:
        
        print_results()
        return
    
    for i in range(1, n + 1):
        results.append(i)
        make(curr_num + 1)
        results.pop()

    return


make(1)