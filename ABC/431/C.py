N, M, K = [int(x) for x in input().split()]
H = list(map(int, input().split()))
B = list(map(int, input().split()))

H.sort()
B.sort()

count = 0
h_ptr = 0
b_ptr = 0

while h_ptr < len(H) and b_ptr < len(B) and count < K:
    head = H[h_ptr]
    body = B[b_ptr]

    # 組み合わせが適切な場合
    if head <= body:
        count += 1
        h_ptr += 1
        b_ptr += 1
    # 組み合わせが不適切な場合
    else:
        b_ptr += 1

# K個適切な組み合わせをつくれたかの判定
if count == K:
    print("Yes")
else:
    print("No")
