# ▣ 입력설명
# 첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N)이 주어집니다.
#
# ▣ 출력설명
# 첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다.
# 출력 순서는 사전순으로 오름차순으로 출력합니다.
#
# ▣ 입력예제 1
# 4 2
#
# ▣ 출력예제 1
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4
# 6

def DFS(L, s):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end=' ')
        cnt += 1
        print()

    else:
        for i in range(s, n + 1):
            res[L] = i # 조합으로 뽑힌 것 저장함
            DFS(L + 1, i + 1)


if __name__ == "__main__":
    n, m = map(int, input().split()) # n개중 m개를 뽑아
    res = [0] * n
    cnt = 0
    DFS(0, 1)
    print(cnt)
