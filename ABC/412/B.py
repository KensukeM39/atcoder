S = input()
T = input()
ans = ""

for i in range(1, len(S)):
    count = 0
    if S[i].isupper():
        for j in range(len(T)):
            if T[j] == S[i-1]:
                count += 1
        if count < 1:
            ans = "No"
            break

if ans != "No":
    ans = "Yes"

print(ans)
