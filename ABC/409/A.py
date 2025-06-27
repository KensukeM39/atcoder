N = int(input())
T = list(input())
A = list(input())

for i in range(N):
  if T[i] == A[i] and T[i] == 'o':
    print("Yes")
    break
  if i == N - 1:
    print("No")
