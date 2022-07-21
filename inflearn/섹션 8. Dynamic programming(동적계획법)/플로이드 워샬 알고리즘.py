# ▣ 입력설명
# 첫 번째 줄에는 도시의 수N(N<=100)과 도로수 M(M<=200)가 주어지고, M줄에 걸쳐 도로정보 와 비용(20 이하의 자연수)이 주어진다. 만약 1번 도시와 2번도시가 연결되고 그 비용이 13이 면 “1 2 13”으로 주어진다.
#
# ▣ 출력설명
# 모든 도시에서 모든 도시로 이동하는데 드는 최소 비용을 아래와 같이 출력한다.
# 자기자신으로 가는 비용은 0입니다. i번 정점에서 j번 정점으로 갈 수 없을 때는 비용을 “M"으 로 출력합니다.
#
# ▣ 입력예제 1
# 5 8
# 1 2 6
# 1 3 3
# 3 2 2
# 2 4 1
# 2 5 13
# 3 4 5
# 4 2 3
# 4 5 7
#
# ▣ 출력예제 1
# 0 5 3 6 13 //1번 정점에서 2번정점으로 5, 1에서 3번 정점으로 3, 1에서 4번 정점으로 6...... M 0 M 1 8
# M 2 0 3 10 //2번 정점에서 1번 정점으로는 갈수 없으므로 “M", .......
# M 3 M 0 7
# M M M M 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    dis = [[5000] * (n + 1) for _ in range(n + 1)] # 연결되어있지 X -> 5000
    for i in range(1, n + 1):
        dis[i][i] = 0

    # i -> j로 직행했을 때
    for i in range(m):
        a, b, c = map(int, input().split())
        dis[a][b] = c

    # i -> k -> j 플로이드 와샬
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    # 출력을 위함
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dis[i][j] == 5000:
                print("M", end=' ')
            else:
                print(dis[i][j], end=' ')
        print()