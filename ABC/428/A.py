S, A, B, X = [int(x) for x in input().split()]

sec = 0
dist = 0

while sec < X:
    if sec + A >= X:
        dist += S * (X - sec)
        break
    else:
        dist += S * A
        sec += A + B

print(dist)