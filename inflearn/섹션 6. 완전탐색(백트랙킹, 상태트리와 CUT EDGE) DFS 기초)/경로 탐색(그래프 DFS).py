# ▣ 입력예제 1
# 5 9
# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 5
# 3 4
# 4 2
# 4 5
#
# ▣ 출력예제 1
# 6

# 한번 방문한 노드는 방문하면 안됨 (체크 리스트 활용)

def DFS(v):
    global cnt
    if v == n:
        cnt += 1
        for x in path:
            print(x, end=' ')
        print()

    else:
        for i in range(1, n + 1):
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i] = 0 # back 하면서 체크 풀기


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]
    ch = [0] * (n + 1)

    # 인접행렬 나타내기
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    cnt = 0
    path = [] # 경로 저장
    path.append(1)
    ch[1] = 1
    DFS(1)
    print(cnt)
