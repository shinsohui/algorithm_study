# ▣ 입력설명
# 첫 번째 줄에 전체 일의 개수 N과 일의 순서 정보의 개수 M이 주어집니다.
# 두 번째 줄부터 M개의 정보가 주어집니다.
#
# ▣ 출력설명
# 전체 일의 순서를 출력합니다.
#
# ▣ 입력예제 1
# 6 6
# 1 4
# 5 4
# 4 3
# 2 5
# 2 3
# 6 2
#
# ▣ 출력예제 1
# 1 6 2 5 4 3

from collections import deque
n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
degree = [0] * (n + 1)
dQ = deque()

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    degree[b] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        dQ.append(i)

while dQ:
    x = dQ.popleft()
    print(x, end=' ')

    # x로 인해 생긴 진입차수 값들을 모두 감소시
    for i in range(1, n + 1):
        if graph[x][i] == 1:
            degree[i] -= 1
            if degree[i] == 0:
                dQ.append(i)
