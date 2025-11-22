N  = int(input())
A = list(map(int, input().split()))



for i in range(N):
    index = -1

    for j in range(i - 1, -1, -1):
        if A[j] > A[i]:
            index = j + 1
            break
    
    print(index)
