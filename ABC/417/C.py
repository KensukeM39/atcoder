N = int(input())
A = []
tmp = list(map(int,input().split()))
for i in range(len(tmp)):
  A.append(tmp[i])

count = 0

for i in range(len(A)):
  for j in range(len(A)):
    if (j+1) - (i+1) == A[i] + A[j]:
    #   print(f'{j+1} - {i+1} = {A[i]} + {A[j]}')
    #   print(j+1, i+1, A[i], A[j])
    #   print((j+1) - (i+1), (A[i] + A[j]))
    #   print()
      count += 1

print(count)