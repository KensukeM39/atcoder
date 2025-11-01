N, M = [int(x) for x in input().split()]
S = []

for a in range(N):
    S.append(input())

set = set()

for i in range(N - M + 1):
    for j in range(N - M + 1):
        patterns = []
        for k in range(i, i + M):
            row = S[k][j : j + M]
            patterns.append(row)
        
        patterns_cnv = tuple(patterns)
        set.add(patterns_cnv)

print(len(set))
