# ▣ 입력설명
# 첫 번째 줄에는 동전의 종류개수 N(1<=N<=12)이 주어진다. 두 번째 줄에는 N개의 동전의 종 류가 주어지고, 그 다음줄에 거슬러 줄 금액 M(1<=M<=500)이 주어진다.
# 각 동전의 종류는 100원을 넘지 않는다.
#
# ▣ 출력설명
# 첫 번째 줄에 거슬러 줄 동전의 최소개수를 출력한다.
#
# ▣ 입력예제 1
# 3
# 1 2 5
# 15
#
# ▣ 출력예제 1
# 3

if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    dy = [1000] * (m + 1)
    dy[0] = 0

    for i in range(n):
        for j in range(coin[i], m+1):
            dy[j] = min(dy[j], dy[j - coin[i]] + 1)
    print(dy[m])