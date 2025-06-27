N = int(input())
D = list(map(int, input().split()))

# print("N=", N)
# print("D=", D)

for i in range(0, N-1):
  total_D = 0
  for k in range(i, N-1):
    total_D += D[k]
    print(total_D, end=(" "))
  print()
  
  # for k in range(i+1, len(D)):
  #   print(i, len(D))
  # D[i] - D[i+1]