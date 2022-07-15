# ▣ 입력설명
# 첫 번째 줄에 자연수 K(3<=K<=13)이 주어집니다.
# 두 번째 줄에 K개의 각 추의 무게가 공백을 사이에 두고 주어집니다. 각 추의 무게는 1부터 200,000까지이다.
#
# ▣ 출력설명
# 첫 번째 측정이 불가능한 가지수를 출력하세요.
#
# ▣ 입력예제 1
# 3
# 1 5 7
#
# ▣ 출력예제 1
# 2

def DFS(L, sum):
    global res
    if L == n:
        if 0 < sum <= s:
            res.add(sum)

    else:
        DFS(L + 1, sum + G[L])
        DFS(L + 1, sum - G[L])
        DFS(L + 1, sum)


if __name__ == "__main__":
    n = int(input())
    G = list(map(int, input().split()))
    s = sum(G)
    res = set()  # 측정될 수 있는 물의 무게 추가
    DFS(0, 0)
    print(s - len(res))