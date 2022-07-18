# ▣ 입력설명
# 첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다.
# N은 2 이상 100 이하의 정수이다.
# 둘째 줄부터 N 개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다.
# 각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N 개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다.
# 높이는 1이상 100 이하의 정수이다.
#
# ▣ 출력설명
# 첫째 줄에 장마철에 물에 잠기지 않는 안전한영역의 최대 개수를 출력한다.
#
# ▣ 입력예제 1
# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7
#
# ▣ 출력예제 1
# 5

import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

sys.setrecursionlimit(10 ** 6)


def DFS(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > h:
            DFS(xx, yy, h)


if __name__ == "__main__":
    n = int(input())
    cnt = 0
    res = 0  # 최대 안전 영역의 개수
    board = [list(map(int, input().split())) for _ in range(n)]

    for h in range(100):  # 높이가 초기화 될 때마다 ch 배열 초기화
        ch = [[0] * n for _ in range(n)]
        cnt = 0  # cnt 초기화, 새로운 안전 영역의 개수를 세기 위함
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0 and board[i][j] > h:  # 물에 안잠긴 부분
                    cnt += 1  # 안전 영역의 개수
                    DFS(i, j, h)

        res = max(res, cnt)  # 최대값

        if cnt == 0:  # 모든 영역의 높이 비의 양보다 작다면
            break

    print(res)
