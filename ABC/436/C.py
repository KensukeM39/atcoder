N, M = [int(x) for x in input().split()]

blocks = set()
result = 0

for _ in range(M):
    R, C = [int(x)-1 for x in input().split()]

    if R + 1 >= N or C + 1 >= N:
        continue

    area = [
        (R, C),
        (R, C+1),
        (R+1, C),
        (R+1, C+1)
    ]

    place = True

    for point in area:
        if point in blocks:
            place = False
            break
    
    if place:
        for point in area:
            blocks.add(point)
        result += 1

print(result)   
