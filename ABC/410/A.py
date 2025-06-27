N = int(input())
A = list(map(int, input().split()))
K = int(input())
c = 0

for i in range(N):
  if K <= A[i]:
    c += 1

print(c)