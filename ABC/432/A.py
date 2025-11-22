numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
print(*numbers, sep="")
