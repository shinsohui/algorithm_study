# ▣ 입력설명
# 첫 줄에는 상자의 크기를 나타내는 두 정수 M, N이 주어진다. M은 상자의 가로 칸의 수, N 은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M, N ≤ 1,000 이다.
# 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄 에는 상자에 담긴 토마토의 정보가 주어진다.
# 하나의 줄에는 상자 가로줄에 들어있는 토마토 의 상태가 M개의 정수로 주어진다.
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
#
# ▣ 출력설명
# 여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다.
# 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
#
# ▣ 입력예제 1
# 6 4
# 0 0 -1 0 0 0
# 0 0 1 0 -1 0
# 0 0 -1 0 0 0
# 0 0 0 0 -1 1
#
# 출력예제 1
# 4

import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
Q = deque()

dis = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(m):
        if board[i][j] == 1:
            Q.append((i, j))

while Q:
    tmp = Q.popleft()

    for i in range(4):
        xx = tmp[0] + dx[i]
        yy = tmp[1] + dy[i]

        if 0 <= xx < m and 0 <= yy < n and board[xx][yy] == 0:
            board[xx][yy] = 1
            dis[xx][yy] = dis[tmp[0]][tmp[1]] + 1
            Q.append((xx, yy))

flag = 1
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            flat = 0

result = 0
if flag == 1:
    for i in range(m):
        for j in range(n):
            if dis[i][j] > result:
                result = dis[i][j]

    print(result)

else:
    print(-1)
