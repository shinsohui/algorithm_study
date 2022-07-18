# ▣ 입력설명
# 첫 번째 줄에 N(5<=N<=13)주어지고, N*N의 지도정보가 N줄에 걸쳐 주어진다.
#
# ▣ 출력설명
# 등산경로의 가지수를 출력한다.
#
# ▣ 입력예제 1
# 5
# 2 23 92 78 93
# 59 50 48 90 80
# 30 53 70 75 96
# 94 91 82 89 93
# 97 98 95 96 100
#
# ▣ 출력예제 1
# 5

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    result = []
    global cnt
    if x == ex and y == ey:
        cnt += 1
    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > board[x][y]:
                ch[xx][yy] = 1
                DFS(xx, yy)
                ch[xx][yy] = 0


if __name__ == "__main__":
    n = int(input())
    board = [[0] * n for _ in range(n)]
    ch = [[0] * n for _ in range(n)]
    cnt = 0
    max = -2147000000
    min = 2147000000

    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            # 최대, 최소값 갱신하기
            if tmp[j] < min:
                min = tmp[j]
                sx = i
                sy = j
            if tmp[j] > max:
                max = tmp[j]
                ex = i
                ey = j
            board[i][j] = tmp[j]
    ch[sx][sy] = 1 # 가장 최소인 값에서 시작하므로 방문 처리
    DFS(sx, sy)
    print(cnt)
