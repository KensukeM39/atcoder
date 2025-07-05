## 実行時間オーバー

A = []
Q = int(input())
query = []

for i in range(Q):
  num = input()
  nums_list = [int(x) for x in num.split()]
  query.append(nums_list)
  
  if query[i][0] == 1:
    for j in range(query[i][1]):
      A.append(query[i][2])
  elif query[i][0] == 2:
    num = query[i][1]
    rmv_num = A[:num]
    A = A[num:]
    total = sum(map(int, rmv_num))
    print(total)
