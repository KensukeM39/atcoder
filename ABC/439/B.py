N = input()
result = 0
numbers = []

while True:
    for i in N:
        result += int(i) ** 2

    if result in numbers:
        print("No")
        break
    elif result == 1:
        print("Yes")
        break
    else:
        numbers.append(result)
        N = str(result)
        result = 0
