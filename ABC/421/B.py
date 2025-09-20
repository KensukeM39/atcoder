num_list = list(map(int, input().split()))

for i in range(3, 11):
    sum = num_list[i - 2] + num_list[i - 3]
    s_x = str(sum)
    f_x = int(s_x[::-1])
    num_list.append(f_x)

print(num_list[9])