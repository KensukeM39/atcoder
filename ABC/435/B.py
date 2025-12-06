N = int(input())
A = list(map(int, input().split()))
result = 0

# print()

# ポインタループ
for l in range(N):
    sum = A[l]

    for r in range(l+1, N, 1):
        # 合計値
        sum += A[r]
        judge = 1

        # print(f'sum = {sum}')

        #約数チェック用
        for i in range(l, r+1, 1):
            # print(f'{sum} // {A[i]} = {sum // A[i]}, {sum % A[i]}')

            if sum % A[i] == 0:
                judge = 0
                break
            else:
                pass
        
        # print(f'{l}, {r}, judge = {judge}')

        if judge == 1:
            result += 1
        
        # print()

print(result)