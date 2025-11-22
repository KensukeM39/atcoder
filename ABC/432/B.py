X = input()
numbers = []

for num in X:
    numbers.append(int(num))

numbers.sort()
tmp = 0
count = 0

for i in range(len(numbers)):
    if numbers[i] == 0:
        count += 1
        pass
    elif numbers[i] != 0 and count >= 1:
        tmp = numbers[0]
        numbers[0] = numbers[i]
        numbers[i] = tmp
        break
    elif numbers[i] != 0 and count == 0:
        break

print(*numbers, sep="")