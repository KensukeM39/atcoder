import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

posA = [i for i, ch in enumerate(S) if ch == 'A']

# パターン1: "ABAB..."
target1 = [i * 2 for i in range(N)]
cost1 = sum(abs(p - t) for p, t in zip(posA, target1))

# パターン2: "BABA..."
target2 = [i * 2 + 1 for i in range(N)]
cost2 = sum(abs(p - t) for p, t in zip(posA, target2))

print(min(cost1, cost2))