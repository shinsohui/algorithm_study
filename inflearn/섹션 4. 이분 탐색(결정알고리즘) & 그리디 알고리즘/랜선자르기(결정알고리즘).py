# ▣ 입력설명
# 첫째 줄에는 엘리트학원이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다. K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 그리고 항상 K ≦ N 이다. 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의   이하의 자연수로 주어진다.
#
# ▣ 출력설명
# 첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.
#
# ▣ 입력예제 1
# 4 11
# 802
# 743
# 457
# 539
#
# ▣ 출력예제 1
# 200

# 몇개의 랜선을 만들 수 있는지 체
def Count(len):
    cnt = 0
    for x in Line:
        cnt += (x // len)
    return cnt


k, n = map(int, input().split())
Line = []
res = 0
largest = 0

for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)

lt = 1
rt = largest

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:  # 랜선의 길이가 너무 긺
        rt = mid - 1

print(res)
