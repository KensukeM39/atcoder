tmp = list(map(int, input().split()))
N = tmp[0]
M = tmp[1]
A = []
B = []
tmp = list(map(int, input().split()))

for i in range(N):
    A.append(tmp[i])

tmp = list(map(int, input().split()))

for i in range(len(tmp)):
    B.append(tmp[i])

for i in range(M):
    for j in range(len(A)):
        if A[j] == B[i]:
            A = A[:j] + A[j+1:]
            break

print(' '.join(map(str, A)))
