S = input()
count = 0
array = []

for i in range(len(S)):
  if S[i] == "#":
    array.append(i+1)
    count += 1
  
  if count == 2:
    print(*array, sep=",")
    count = 0
    array.clear()
