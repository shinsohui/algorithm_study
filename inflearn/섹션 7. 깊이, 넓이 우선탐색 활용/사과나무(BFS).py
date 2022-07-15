# ▣ 입력설명
# 첫 줄에 자연수 N(홀수)이 주어진다.(3<=N<=20)
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
# 이 자연수는 각 격자안에 있는 사과나무에 열린 사과의 개수이다.
# 각 격자안의 사과의 개수는 100을 넘지 않는다.
#
# ▣ 출력설명
# 수확한 사과의 총 개수를 출력합니다.
#
# ▣ 입력예제 1
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
#
# ▣ 출력예제 1
# 379

from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

ch = [[0] * n for _ in range(n)]
sum = 0
Q = deque()
ch[n//2][n//2] = 1
sum += a[n//2][n//2]
Q.append((n//2, n//2))

L = 0

while True:
    if L == n//2: # 레벨이 2일 때
        break
    size = len(Q)

    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] * dy[j]
            if ch[x][y] == 0:
                sum += a[x][y]
                ch[x][y] = 1
                Q.append((x, y))
    L += 1

print(sum)