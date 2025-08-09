tmp = list(map(int, input().split()))
N = tmp[0]
A = tmp[1]
B = tmp[2]
S = input()

print(f'{S[A:N-B]}')