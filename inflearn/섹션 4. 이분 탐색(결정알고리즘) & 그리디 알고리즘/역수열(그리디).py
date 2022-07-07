# ▣ 입력설명
# 첫번째 줄에 자연수 N(3<=N<100)이 주어지고, 두번째 줄에는 역수열이 숫자 사이에 한칸의 공백을 두고 주어진다.
#
# ▣ 출력설명
# 원래 수열을 출력합니다.
#
# ▣ 입력예제 1
# 8
# 5 3 4 0 2 1 1 0
#
# ▣ 출력예제 1
# 4 8 6 2 5 1 3 7

n = int(input())
a = list(map(int, input().split())) # 역수열
seq = [0]*n
for i in range(n):
    for j in range(n):
        if a[i] == 0 and seq[j] == 0:
            seq[j] = j+1
            break
        elif seq[j] == 0:
            a[i] -= 1

for x in seq:
    print(x, end=' ')


