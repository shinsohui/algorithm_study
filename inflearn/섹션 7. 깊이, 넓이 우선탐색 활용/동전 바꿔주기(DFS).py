# ▣ 입력설명
# 첫째 줄에는지폐의 금액 T(0<T≤10,000), 둘째 줄에는 동전의 가지 수k(0<k≤10), 셋째 줄부터 마지막 줄까지는 각 줄에 동전의금액 pi(0<pi≤T)와 개수 ni(0<ni≤10)가 주어진다.
# pi와 ni 사이 에는 빈 칸이 하나씩 있다.
#
# ▣ 출력설명
# 첫 번째 줄에 동전 교환 방법의 가지 수를 출력한다.(교환할 수 없는 경우는 존재하지 않는 다.)
#
# ▣ 입력예제 1
# 20
# 3
# 5 3
# 10 2
# 1 5
#
# ▣ 출력예제 1
# 4

def DFS(L, sum):
    global cnt

    if sum > T:
        return

    if L == k:
        if sum == T:
            cnt += 1
    else:
        for i in range(cn[L] + 1):
            DFS(L + 1, sum + cv[L] * i)


if __name__ == "__main__":
    T = int(input())
    k = int(input())
    cv = list()
    cn = list()

    for i in range(k):
        a, b = map(int, input().split())
        cv.append(a) # 동전의 금액
        cn.append(b) # 동전의 개수

    cnt = 0
    DFS(0, 0)
    print(cnt)