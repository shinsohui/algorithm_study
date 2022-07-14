# ▣ 입력설명
# 첫째 줄에 두개의 정수 N(1≤N≤10)과 F가 주어진다. N은 가장 윗줄에 있는 숫자의 개수를 의 미하며 F는 가장 밑에 줄에 있는 수로 1,000,000 이하이다.
#
# ▣ 출력설명
# 첫째 줄에 삼각형에서 가장 위에 들어갈 N개의 숫자를 빈 칸을 사이에 두고 출력한다. 답이 존재 하지 않는 경우는 입력으로 주어지지 않는다.
#
# ▣ 입력예제 1
# 4 16
#
# ▣ 출력예제 1
# 3 1 2 4
import sys


def DFS(L, sum):
    if L == n and sum == f:
        for x in p:
            print(x, end=' ')
        print()
        sys.exit(0)

    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L + 1, sum + (p[L] * b[L]))
                ch[i] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())
    p = [0] * n
    b = [1] * n
    ch = [0] * (n + 1)

    # 이항계수 초기화
    for i in range(1, n):
        b[i] = b[i - 1] * (n - i) // i

    DFS(0, 0)
