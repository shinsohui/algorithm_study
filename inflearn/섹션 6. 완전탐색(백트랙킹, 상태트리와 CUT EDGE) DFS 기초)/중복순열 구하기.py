# ▣ 입력설명
# 첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.
#
# ▣ 출력설명
# 첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다.
# 출력순서는 사전순으로 오름차순으로 출력합니다.
#
# ▣ 입력예제 1
# 3 2
#
# ▣ 출력예제 1
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3
# 9

import sys
input = sys.stdin.readline

def DFS(L):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1

    else:
        for i in range(1, n+1):
            res[L] = i
            DFS(L+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)



