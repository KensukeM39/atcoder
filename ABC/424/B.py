N, M, K = [int(x) for x in input().split()]
ans_list = [0] * N      # 人数分の正解した問題の総和を格納するリスト
sum_of_prob = M * (M + 1) // 2      # 全問正解の場合の総和
result = []

for i in range(K):
    man, prob = list(map(int, input().split()))
    ans_list[man - 1] += prob

    if ans_list[man - 1] == sum_of_prob:
        result.append(man)

if result != []:
    print(*result)
