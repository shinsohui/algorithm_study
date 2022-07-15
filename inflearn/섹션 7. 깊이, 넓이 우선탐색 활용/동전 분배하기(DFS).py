# ▣ 입력설명
# 첫째 줄에는 동전의 개수 N(3<=N<=12)이 주어집니다.
# 그 다음 N줄에 걸쳐 각 동전의 금액이 주어집니다.
#
# ▣ 출력설명
# 총액이 가장 큰 사람과 가장 작은 사람의 최소차를 출력하세요.
#
# ▣ 입력예제 1
# 7
# 8
# 9
# 11
# 12
# 23
# 15
# 17
#
# ▣ 출력예제 1
# 5


def DFS(L):
    global res
    if L == n:
        cha = max(money) - min(money)
        if cha < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = cha
    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L + 1)
            money[i] -= coin[L] # 더했던 동전 금액을 빼줘야 함


if __name__ == "__main__":
    coin = []
    money = [0] * 3  # A, B, C 세 사람에게 분배된 금액을 계산

    n = int(input())
    for i in range(n):
        coin.append(int(input()))

    res = 2147000000

    DFS(0)
    print(res)