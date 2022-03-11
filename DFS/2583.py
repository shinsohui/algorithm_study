from collections import deque

M, N, K = map(int, input().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

graph = [list([0] * N) for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = -1

resultList = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            count = 1
            queue = deque([])
            queue.append([i, j])
            graph[i][j] = count

            while queue:
                y, x = queue.popleft()
                for k in range(4):
                    nY = y + dy[k]
                    nX = x + dx[k]

                    if 0 <= nX < N and 0 <= nY < M and graph[nY][nX] == 0:
                        graph[nY][nX] = 1
                        queue.append([nY, nX])
                        count += 1

            resultList.append(count)

print(len(resultList))
resultList.sort()
for num in resultList:
    print(num,end=" ")