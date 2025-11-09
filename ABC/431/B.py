X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())

index = []
weight = X

for _ in range(Q):
    P = int(input()) - 1

    # 取り付けられている部品の種類のインデックスを格納
    if P not in index:
        weight += W[P]
        index.append(P)
    # 部品を取り外す
    elif P in index:
        weight -= W[P]
        index.remove(P)
    
    print(weight)