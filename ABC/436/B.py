N = int(input())
matrix = [[None] * (N) for _ in range(N)]

count = N ** 2 - 1

i = 0
j = (N - 1) // 2

matrix[i][j] = 1

r = i
c = j
k = 1

for _ in range(count):
    
    i = (r - 1) % N
    j = (c + 1) % N
    k += 1
    
    if matrix[i][j] == None:
        matrix[i][j] = k
        r = i
        c = j
    else:
        i = (r + 1) % N
        j = c
        matrix[i][j] = k
        r = i

for row in matrix:
    print(*row)
