N, Q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

for _ in range(Q):
    tmp = [int(x) for x in input().split()]
    sum = 0

    if tmp[0] == 1:
        c = tmp[1]
        for _ in range(c):
            A.append(A.pop(0))
    
    else:
        l = tmp[1]
        r = tmp[2]
        for i in range(l - 1, r):
            sum += A[i]
            # print(f'{i}: {A[i]} | {sum}')
        
        print(sum)

    # print(A)
