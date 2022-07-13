# ▣ 입력설명
# 첫 줄에 한 줄에 필수과목의 순서가 주어집니다. 모든 과목은 영문 대문자입니다.
# 두 번째 줄에 N(1<=N<=10)이 주어집니다.
# 세 번 째 줄부터 현수가 짠 N개의 수업설계가 주어집니다.(수업설계의 길이는 30이하이다).
# 수업설계는 같은 과목을 여러 번 이수하도록 설계해도 됩니다.
#
# ▣ 출력설명
# 수업설계가 잘된 것이면 "YES", 잘못된 것이면 "NO"를 출력합니다.
#
# ▣ 입력예제 1
# CBA
# 3
# CBDAGE
# FGCDAB
# CTSBDEA
#
# ▣ 출력예제 1
# #1 YES
# #2 NO
# #3 YES
#
# ▣ 입력예제 2
# AFC
# 1
# AFFDCCFF
#
# ▣ 출력예제 2
# #1 YES

from collections import deque

need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need)

    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" % (i + 1))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" % (i + 1))
        else:
            print("#%d NO" % (i + 1))
