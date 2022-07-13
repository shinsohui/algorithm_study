# ▣ 입력설명
# 첫 줄에 자연수 N(5<=N<=1,000)과 K(2<=K<=9)가 주어진다.
#
# ▣ 출력설명
# 첫 줄에 마지막 남은 왕자의 번호를 출력합니다.
#
# ▣ 입력예제 1
# 8 3
#
# ▣ 출력예제 1
# 7

# 앞에서 빼서 뒤로 넣기
from collections import deque
n, k = map(int, input().split())
dq = list(range(1, n+1))
dq = deque(dq)

while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()

    if len(dq) == 1:
        print(dq[0])
        dq.popleft()

