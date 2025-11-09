H, B = [int(x) for x in input().split()]

if H > B:
    print(abs(H - B))
else:
    print(0)