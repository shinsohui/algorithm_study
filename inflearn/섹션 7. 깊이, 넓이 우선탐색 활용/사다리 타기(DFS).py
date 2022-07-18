# ▣ 입력설명
# 10*10의 사다리 지도가 주어집니다.
#
# ▣ 출력설명
# 출발지 열 번호를 출력하세요.
#
# ▣ 입력예제 1
# 1 0 1 0 0 1 0 1 0 1
# 1 0 1 1 1 1 0 1 0 1
# 1 0 1 0 0 1 0 1 0 1
# 1 0 1 0 0 1 0 1 1 1
# 1 0 1 0 0 1 0 1 0 1
# 1 0 1 1 1 1 0 1 0 1
# 1 0 1 0 0 1 0 1 1 1
# 1 1 1 0 0 1 0 1 0 1
# 1 0 1 0 0 1 1 1 0 1
# 1 0 1 0 0 2 0 1 0 1
#
# ▣ 출력예제 1
# 7

def DFS(x, y):
    ch[x][y] = 1

    if x == 0:
        print(y)
    else:
        # 왼쪽을 먼저 본다.
        if y - 1 > 0 and board[x][y-1] == 1 and ch[x][y-1] == 0:
            DFS(x, y-1)
        # 오른쪽을 본다.
        elif y + 1 < 10 and board[x][y+1] == 1 and ch[x][y+1] == 0:
            DFS(x, y+1)
        else:
            DFS(x -1, y)


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(10)]
    ch = [[0] * 10 for _ in range(10)]

    for y in range(10):
        if board[9][y] == 2:
            DFS(9, y)