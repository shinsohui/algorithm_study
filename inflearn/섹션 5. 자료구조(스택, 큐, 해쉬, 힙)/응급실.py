# ▣ 입력설명
# 첫 줄에 자연수 N(5<=N<=100)과 M(0<=M<N) 주어집니다.
# 두 번째 줄에 접수한 순서대로 환자의 위험도(50<=위험도<=100)가 주어집니다.
# 위험도는 값이 높을 수록 더 위험하다는 뜻입니다. 같은 값의 위험도가 존재할 수 있습니다.
#
# ▣ 출력설명
# M번째 환자의 몇 번째로 진료받는지 출력하세요.
#
# ▣ 입력예제 1
# 5 2
# 60 50 70 80 90
#
# ▣ 출력예제 1
# 3
#
# ▣ 입력예제 2
# 6 0
# 60 60 90 60 60 60
#
# ▣ 출력예제 2
# 5

from collections import deque

n, m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
# [(0, 60), (1, 50), (2, 70), (3, 80), (4, 90)]

Q = deque(Q)
cnt = 0

while True:
    cur = Q.popleft()
    if any(cur[1] < x[1] for x in Q):  # 위험도 검사
        Q.append(cur)  # 이 사람보다 더 높은 위험도를 가지면 그대로 뒤로 이동
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break
