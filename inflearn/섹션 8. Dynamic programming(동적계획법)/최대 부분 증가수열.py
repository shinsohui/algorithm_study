# ▣ 입력설명
# 첫째 줄은 입력되는 데이터의 수 N(2≤N≤1,000, 자연수)를 의미하고, 둘째 줄은 N개의 입력데이터들이 주어진다.
#
# ▣ 출력설명
# 첫 번째 줄에 부분증가수열의 최대 길이를 출력한다.
#
# ▣ 입력예제 1
# 8
# 5 3 7 8 6 2 9 4
#
# ▣ 출력예제 1
# 4

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dy = [0] * (n + 1)
dy[1] = 1
res = 0

for i in range(2, n + 1):
    max = 0
    for j in range(i - 1, 0, -1):
        if arr[j] < arr[i] and dy[j] > max:
            max = dy[j]

    dy[i] = max + 1
    if dy[i] > res:
        res = dy[i]

print(res)
