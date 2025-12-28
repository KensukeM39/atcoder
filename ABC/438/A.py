D, F = [int(x) for x in input().split()]

total = (D - F) // 7 
last = F + (total * 7)
next = last + 7
result = next - D

print(result)