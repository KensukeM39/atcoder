S = input()
index_t = []
rate = float(1)

for i in range(len(S)):
    if S[i] == "t":
        index_t.append(i)

if index_t == []:
    rate = 0
else:
    t = S[min(index_t):max(index_t)+1]

    if len(t) >= 3:
        x = len(index_t)
        rate = (x - 2) / (len(t) - 2)
    else:
        rate = 0

print(f"{round(rate, 17):.17f}")