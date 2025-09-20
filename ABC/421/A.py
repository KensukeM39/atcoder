N = int(input())
S = []

for i in range(N):
  tmp = input()
  S.append(tmp)

tmp = list(input().split())
X = int(tmp[0])
Y = tmp[1]

if S[X-1] == Y:
  print("Yes")
else:
  print("No")