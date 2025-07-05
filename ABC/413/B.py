N = int(input())
S = []
result = []

for i in range(N):
  string  = input()
  S.append(string)

for i in range(N):
  for j in range(N):
    if j != i:
      judge = 0
      string = S[i] + S[j]
      for k in range(len(result)):
        if result[k] == string:
          judge = 1
          break
      if judge != 1:
        result.append(string)

print(len(result))