# ▣ 입력설명
# 첫 번째줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력 되고 그 다음 N줄에는 각각 N개의 자료(0 혹은 1)가 입력된다
#
# ▣ 출력설명
# 첫 번째줄에는 총 단지수를 출력하시오. 그리고 각 단지내의 집의 수를 오름차순으로 정렬하 여 한줄에 하나씩 출력하시오
#
# ▣ 입력예제 1
# 7
# 0 1 1 0 1 0 0
# 0 1 1 0 1 0 1
# 1 1 1 0 1 0 1
# 0 0 0 0 1 1 1
# 0 1 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 1 1 1 0 0 0
#
# ▣ 출력예제 1
# 3
# 7
# 8
# 9

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt
    cnt += 1
    board[x][y] = 0 # 중복 방문 방지

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1:
            DFS(xx, yy)


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = [] # 한 단지내의 집의 개수
    # 한 행씩 처음 단지가 시작되는 지점을 찾는다.
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt = 0
                DFS(i, j)
                res.append(cnt)

    print(len(res))
    res.sort()
    for x in res:
        print(x)
