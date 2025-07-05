N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

weight = 0

for i in range(N):
  weight += A[i]

if weight <= M:
  print("Yes")
else:
  print("No")