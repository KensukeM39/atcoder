## メモリオーバー

def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

A = int(input())    # A進数
N = int(input())    # 整数 N
sum = 0

for i in range(N+1):  # 0~Nまで回す
  str_num = str(i)
  half_digit = (len(str_num) + 1) // 2  # 10進数の回文判定の準備
  judge = 1
  
  # 10進法で回文の場合
  for j in range(half_digit):
    # print(str_num, str_num[j], str_num[-j-1])
    if str_num[j] != str_num[-j-1]:     # 10進数が回文でない場合は終了
      judge = 0
      break
  
  # 10進法の回文判定
  if judge == 1:                        # 10進数が回文の場合
    print(i)
    
    num = base10int(i,A)                # iをA進数に変換
    base = str(num)
    # print(base)
    half_digit = (len(base) + 1) // 2   # A進数の回文判定の準備
    
    # A進法で回文の場合
    for k in range(half_digit):
      if base[k] != base[-k-1]:         # A進数が回文でない場合は終了
        judge = 0
        break
    
    # 10進法の回文判定
    if judge == 1:                      # A進数が回文の場合
      print(base)
      sum += i                          # 総和に追加

print(sum)
