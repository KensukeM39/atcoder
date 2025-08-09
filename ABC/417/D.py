N = int(input())
P = []
A = []
B = []
for i in range(N):
    tmp = list(map(int, input().split()))
    P.append(tmp[0])
    A.append(tmp[1])
    B.append(tmp[2])

Q = int(input())
X = []
for i in range(Q):
    tmp = int(input())
    X.append(tmp)

for i in range(Q):
    for j in range(N):
        if P[j] >= X[i]:
            X[i] += A[j]
        elif P[j] < X[i] and X[i] < B[j]:
            X[i] = 0
        elif P[j] < X[i] and X[i] >= B[j]:
            X[i] -= B[j]
    print(X[i])
