N = int(input())
A = [int(x) for x in input().split()]
num_list = []
judge = True

for i in range(1, N + 1):
    if A.count(i) > 1:
        judge = False
    
    if i not in A:
        num_list.append(i)

replacements = iter(num_list)

if judge:
    print("Yes")
    
    for i in range(len(A)):
        if A[i] == -1:
            try:
                A[i] = next(replacements)
            except StopIteration:
                break
    
    print(*A)

else:
    print("No")