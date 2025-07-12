N  = int(input())
letter = ""

for i in range(N):
  combo = input().split()
  
  for j in range(int(combo[1])):
    letter += combo[0]
    # print(i, j, letter, len(letter))
    
    if len(letter) > 100:
      break
  
  if len(letter) > 100:
    print("Too Long")
    break
  elif i == N-1:
    print(letter)