N = int(input())
learnt_num = []
result = []

for i in range(N):
    tmp = list(map(int, input().split()))
    
    if tmp[0] in learnt_num or tmp[1] in learnt_num:
        learnt_num.append(i + 1)
    elif  tmp == [0, 0]:
        learnt_num.append(i + 1)

print(len(learnt_num))