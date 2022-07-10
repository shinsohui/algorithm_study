import sys
sys.setrecursionlimit(10 ** 9)

def dfs(x, y):

    if x == m - 1 and y == n - 1:
        cnt.append(1)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if graph[x][y] > graph[nx][ny]:
                dfs(nx, ny)


m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = []
dfs(0, 0)
print(len(cnt))