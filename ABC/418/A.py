N = int(input())
S = input()
letter = "tea"
judge = 1

if len(S) >= 3:
  for i in range(len(letter)):
    if letter[i] == S[N-(len(letter)-i)]:
      judge *= 1
    else:
      judge = 0
else:
  judge = 0

if judge == 1:
    print("Yes")
else:
    print("No")