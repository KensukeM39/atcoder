tmp = list(map(int,input().split()))
N = tmp[0]
L = tmp[1]
R = tmp[2]
S = input()
judge = 1

for i in range(L-1,R):
  if S[i] != "o":
    judge = 0

if judge == 1:
  print("Yes")
else:
  print("No")
