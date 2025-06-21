N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))

block = []

for i in range(N):
  block.append(1)

# white block is 1
# black block is -1

for k in range(Q):
  block[A[k]-1] *= -1
  print(A[k], block)
  
  if block[i] == 1:
    
    tie = 0