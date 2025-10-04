S = input()
x = 0
y = 0

for i in range(len(S)):
    judge = S[0]
    if S[i] == judge:
        x += 1
    else:
        tmp = S[i]
        y += 1
    
    if x >= 2 and y == 1:
        print(tmp)
        break
    elif x == 1 and y >= 2:
        print(judge)
        break