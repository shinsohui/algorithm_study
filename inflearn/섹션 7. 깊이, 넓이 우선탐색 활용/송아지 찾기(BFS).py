# ▣ 입력설명
# 첫 번째 줄에 현수의 위치 S와 송아지의 위치 E가 주어진다. 직선의 좌표 점은 1부터 10,000 까지이다.
#
# ▣ 출력설명
# 점프의 최소횟수를 구한다.
#
# ▣ 입력예제 1
# 5 14
#
# ▣ 출력예제 1
# 3

from collections import deque
MAX = 10000
ch = [0] * (MAX + 1)
dis = [0] * (MAX + 1)
n, m = map(int, input().split())
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)

while dQ:
    now = dQ.popleft()

    if now == m:
        break

    for next in (now - 1, now + 1, now + 5): # 세 가닥으로 뻗는다.
        if 0 < next <= MAX:
            if ch[next] == 0:
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1

print(dis[m])


