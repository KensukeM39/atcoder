Q = int(input())
query = []
bag = []

for i in range(Q):
    tmp = list(map(int, input().split()))
    
    if tmp[0] == 1:
        bag.append(tmp[1])
    
    elif tmp[0] == 2:
        if bag == []:
            break
        minimum = min(bag)
        query.append(minimum)
        bag.remove(minimum)

for i in range(len(query)):
    print(query[i])