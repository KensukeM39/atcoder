N, K = [int(x) for x in input().split()]
S = input()

counts = {}

upper = N - K + 1

for i in range(upper):
    sub = S[i : i + K]
    counts[sub] = counts.get(sub, 0) + 1

max_occurrence = 0

if counts:
    max_occurrence = max(counts.values())

print(max_occurrence)

max_substrings = [
    t for t, count in counts.items()
    if count == max_occurrence
]

max_substrings.sort()

for t in max_substrings:
    print(t)
