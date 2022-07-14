# 무방향 그래프
# 5 5
# 1 2
# 1 3
# 2 4
# 3 4
# 4 4

# n, m = map(int, input().split())
# g = [[0] * (n+1) for _ in range((n+1))]
#
# for i in range(m):
#     a, b = map(int, input().split())
#     g[a][b] = 1
#     g[b][a] = 1
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(g[i][j], end=' ')
#     print()

# ▣ 입력예제 1
# 6 9
# 1 2 7
# 1 3 4
# 2 1 2
# 2 3 5
# 2 5 5
# 3 4 5
# 4 2 2
# 4 5 5
# 6 4 5
#
# ▣ 출력예제 1
# 0 7 4 0 0 0
# 2 0 5 0 5 0
# 0 0 0 5 0 0
# 0 2 0 0 5 0
# 0 0 0 0 0 0
# 0 0 0 5 0 0

n, m = map(int, input().split())
g = [[0] * (n+1) for _ in range((n+1))]

for i in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(g[i][j], end=' ')
    print()
