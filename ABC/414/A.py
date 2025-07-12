num = list(map(int,input().split()))
N = num[0]
L = num[1]
R = num[2]
X = []
Y = []
count = 0

for i in range(N):
  time = list(map(int, input().split()))
  # X.append(time[0])
  # Y.append(time[1])
  # print(time[0], time[1])
  if time[0] <= L and time[1] >= R:
    count += 1

print(count)

# print("N,L,R = ",N,L,R)
# print("X = ",X)
# print("Y = ",Y)
