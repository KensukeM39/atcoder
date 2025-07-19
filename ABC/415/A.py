N = int(input())
A = list(map(int, input().split()))
X = int(input())
judge = 0

for i in range(N):
  if A[i] == X:
    judge = 1

if judge == 1:
  print("Yes")
else:
  print("No")