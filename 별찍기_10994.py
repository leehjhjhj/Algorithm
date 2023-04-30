n = int(input())
lens = 4 * n - 3
stars = [[" "] * lens for _ in range(lens)]



def star(n, idx):
    if n == 1:
        stars[idx][idx] = '*'
        return
    
    l = 4 * n - 3

    for i in range(idx, idx + l):
        stars[idx][i] = '*'
        stars[idx + l - 1][i] = '*'
        stars[i][idx] = '*'
        stars[i][idx + l - 1] = '*'

    return star(n - 1, idx + 2)
    
star(n, 0)

for i in range(lens):
    for j in range(lens):
        print(stars[i][j], end='')
    print()


