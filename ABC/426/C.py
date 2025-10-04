N, Q = [int(x) for x in input().split()]

numbers = []
for i in range(N):
    numbers.append(i+1)

count = 0
for i in range(Q):
    judge, latest = list(map(int, input().split()))
    count = 0

    for j in range(N):
        if numbers[j] <= judge:
            numbers[j] = latest
            count += 1

    print(count)
