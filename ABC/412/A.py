N = int(input())
A = []
B = []
count = 0

for i in range(N):
    tmp = list(map(int, input().split()))
    A.append(tmp[0])
    B.append(tmp[1])

for i in range(N):
    if B[i] > A[i]:
        count += 1

print(count)
