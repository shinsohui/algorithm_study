# ▣ 입력설명
# 첫 줄에 자연수 N(3<=N<=200,000)과 C(2<=C<=N)이 공백을 사이에 두고 주어집니다.
# 둘째 줄부터 N개의 줄에 걸쳐 마구간의 좌표 xi(0<=xi<=1,000,000,000)가 한 줄에 하나씩 주어집니다.
#
# ▣ 출력설명
# 첫 줄에 가장 가까운 두 말의 최대 거리를 출력하세요.
#
# ▣ 입력예제 1
# 5 3
# 1
# 2
# 8
# 4
# 9
#
# ▣ 출력예제 1
# 3

def Count(len):
    cnt = 1
    ep = Line[0]
    for i in range(1, n):
        if Line[i] - ep >= len: # 말 배치 가능
            cnt += 1
            ep = Line[i]
    return cnt


n, c = map(int, input().split())
Line = []
for _ in range(n):
    tmp = int(input())
    Line.append(tmp)

Line.sort()
lt = 1
rt = Line[n - 1]

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)