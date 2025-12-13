N = int(input())
S = input()

length = len(S)

add_o = N - length
str_o = "o" * add_o
result = str_o + S

print(result)