N = int(input())
A = [int(x) for x in input().split()]

result = 0
num = 1

for i in range(N):
    num -= 1

    if A[i] >= 2 and A[i] > num:
        num = A[i] - 1
    elif A[i] >= 2 and A[i] <= num:
        pass
    else:
        pass

    result += 1

    if num == 0:
        break

print(result)