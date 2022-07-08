# ▣ 입력설명
# 첫째 줄에 자연수 N(5<=N<=1000)과 M(70<=M<=250)이 주어집니다.
# 두 번째 줄에 N개로 구성된 몸무게 수열이 주어집니다. 몸무게는 50이상 150이하입니다.
# 각 승객의 몸무게는 M을 넘지는 않습니다. 즉 탈출을 못하는 경우는 없습니다.
#
# ▣ 출력설명
# 첫째 줄에 구명보트의 최소 개수를 출력합니다.
#
# ▣ 입력예제 1
# 5 140
# 90 50 70 100 60
#
# ▣ 출력예제 1
# 3

# n, limit = map(int, input().split())
# p = list(map(int, input().split()))
#
# p.sort()
# cnt = 0
#
# while p: # 비어있으면 거짓
#     if len(p) == 1:
#         cnt += 1
#         break
#     if p[0] + p[-1] > limit:
#         p.pop()
#         cnt += 1
#     else:
#         p.pop(0)
#         p.pop()
#         cnt += 1
#
# print(cnt)

# list()는 pop() 할 때마다 배열 원소를 이동시켜 비효율적
# deque() 사용해서 풀기
from collections import deque

n, limit = map(int, input().split())
p = list(map(int, input().split()))

p.sort()
p = deque(p)
cnt = 0
while p:
    if len(p) == 1:
        cnt += 1
        break
    if p[0] + p[-1] > limit:
        p.pop()
        cnt += 1
    else:
        p.popleft()
        p.pop()
        cnt += 1

print(cnt)