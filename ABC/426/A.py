tmp = input().split()

numbers = []

for x in tmp:
    if x == "Ocelot":
        numbers.append(1)
    elif x == "Serval":
        numbers.append(2)
    else:
        numbers.append(3)

X, Y = numbers

if X >= Y:
    print("Yes")
else:
    print("No")