# ▣ 입력설명
# 첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 12)이 주어진다.
# 둘째 줄부터 도시 정보가 입력된다.
#
# ▣ 출력설명
# 첫째 줄에 M개의 피자집이 선택되었을 때 도시의 최소 피자배달거리를 출력한다.
#
# ▣ 입력예제 1
# 4 4
# 0 1 2 0
# 1 0 2 1
# 0 2 1 2
# 2 0 1 2
#
# ▣ 출력예제 1
# 6


def DFS(L, s):
    global res
    if L == m:
        sum = 0
        for z in range(len(hs)): # 집을 정하기
            x1 = hs[z][0] # 현재 집의 위치를 x1
            y1 = hs[z][1] # y1에 저장한다.
            dis = 2147000000

            for x in cb:
                # 피자집의 좌표 구하기
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis, abs(x1-x2) + abs(y1-y2))
            sum += dis

        if sum < res:
            res = sum

    else:
        for i in range(s, len(pz)):
            cb[L] = i
            DFS(L + 1, i + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    hs = []
    pz = []
    cb = [0] * m
    res = 2147000000

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                hs.append((i, j))
            elif board[i][j] == 2:
                pz.append((i, j))
    DFS(0, 0) # 조합 계산
    print(res)