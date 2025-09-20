tmp = list(map(int, input().split()))
N = tmp[0]
M = tmp[1]
S = input()
T = input()
num_list = []

for i in range(M):
    tmp = list(map(int, input().split()))
    num_1 = tmp[0]
    num_2 = tmp[1]
    if num_1 == 1:
        if num_2 == N:
            swap = S
            S = T
            T = swap
        else:
            swap_a1 = ""
            swap_a2 = S[(num_2):]
            swap_b1 = ""
            swap_b2 = T[(num_2):]
            S = swap_b1 + S[(num_1 - 1):num_2] + swap_b2
            T = swap_a1 + T[(num_1 - 1):num_2] + swap_a2

    else:
        if num_1 == N:
            swap_a2 = S[(num_2):]
            swap_b2 = T[(num_2):]
            S = S[:num_2] + swap_b2
            T = T[:num_2] + swap_a2
        else:
            swap_a1 = S[:(num_1 - 1)]
            swap_a2 = S[(num_2):]
            swap_b1 = T[:(num_1 - 1)]
            swap_b2 = T[(num_2):]
            S = swap_b1 + S[(num_1 - 1):num_2] + swap_b2
            T = swap_a1 + T[(num_1 - 1):num_2] + swap_a2

    
print(T)
