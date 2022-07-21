# ▣ 입력설명
# 입력의 첫째 줄에는 회원의 수가 있다.
# 단, 회원의 수는 50명을 넘지 않는다. 둘째 줄 이후로는 한 줄에 두 개의 회원번호가 있는데, 이것은 두 회원이 서로 친구임을 나타낸다. 회원번호는 1부터 회원의 수만큼 번호가 붙어있다. 마지막 줄에는 -1이 두 개 들어있다
#
# ▣ 출력설명
# 첫째 줄은 회장 후보의 점수와 회장후보 수를 출력하고 두 번째 줄은 회장 후보를 모두 출력 한다.
#
# ▣ 입력예제 1
# 5
# 1 2
# 2 3
# 3 4
# 4 5
# 2 4
# 5 3
# -1 -1
#
# ▣ 출력예제 1
# 2 3
# 2 3 4

if __name__ == "__main__":
    n = int(input())
    dis = [[100] * (n + 1) for _ in range(n+1)]
    for i in range(1, n + 1):
        dis[i][i] = 0

    while True:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        dis[a][b] = 1
        dis[b][a] = 1 # 무방향 그래프

    # 플로이드 워샬
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    res = [0] * (n + 1)
    score = 100

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res[i] = max(res[i], dis[i][j])

        score = min(score, res[i])

    out = []

    for i in range(1, n + 1):
        if res[i] == score:
            out.append(i)
    print("%d %d" %(score, len(out)))

    for x in out:
        print(x, end=' ')


