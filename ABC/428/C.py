Q = int(input())
S = []
num = 0
ans = []

bal = 0
min_stack = [0]

for i in range(Q):
    tmp = list(input().split())
    num = 0
    query_type = tmp[0]
    
    if query_type == "1":
        char = tmp[1]
        S.append(char)
        
        if char == '(':
            bal += 1
        else:
            bal -= 1
        
        new_min = min(min_stack[-1], bal)
        min_stack.append(new_min)

    elif query_type == "2":
        removed_char = S.pop()
        
        if removed_char == '(':
            bal -= 1
        else:
            bal += 1
            
        min_stack.pop()
    
    if bal == 0 and min_stack[-1] >= 0:
        ans.append("Yes")
    else:
        ans.append("No")

print('\n'.join(ans))