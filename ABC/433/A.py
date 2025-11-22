X, Y, Z = list(map(int, input().split()))
result = 0

while X < 101 or Y < 101:
    if X == Y * Z:
        result = 1
        break
    else:
        X += 1
        Y += 1

if result == 1:
    print("Yes")
else:
    print("No")