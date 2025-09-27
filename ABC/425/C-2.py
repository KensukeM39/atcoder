N, Q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

S = [0] * (N + 1)
for i in range(N):
    S[i+1] = S[i] + A[i]

shift = 0

for _ in range(Q):
    q = [int(x) for x in input().split()]
    
    if q[0] == 1:
        c = q[1]
        shift = (shift + c) % N
    
    else:
        l, r = q[1] - 1, q[2]
        
        phys_l = (shift + l) % N
        phys_r = (shift + r) % N
        
        ans = 0
        if phys_l < phys_r:
            ans = S[phys_r] - S[phys_l]
        else:
            ans = (S[N] - S[phys_l]) + S[phys_r]
            
        print(ans)