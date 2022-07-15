# ▣ 입력설명
# 첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
# 둘째 줄부터 1일부터 N일까지 순서대로 주어진다. (1 ≤ T ≤ 7, 1 ≤ P ≤ 100)
#
# ▣ 출력설명
# 첫째 줄에 현수가 얻을 수 있는 최대 이익을 출력한다.
#
# ▣ 입력예제 1
# 7
# 4 20
# 2 10
# 3 15
# 3 20
# 2 30
# 2 20
# 1 10
#
# ▣ 출력예제 1
# 60

def DFS(L, sum):
    global res
    if L == n + 1: # 종료 조건 확인
        if sum > res:
            res = sum

    else:
        if L + T[L] <= n + 1:
            DFS(L + T[L], sum + P[L]) # 상담 진행

        else:
            DFS(L + 1, sum) # 상담을 진행하지 않고 넘어감 


if __name__ == "__main__":
    n = int(input())
    T = list()
    P = list()
    for i in range(n):
        a, b = map(int, input().split())
        T.append(a)
        P.append(b)
    res = -2147000000
    T.insert(0, 0)  # 1번 인덱스부터 시작하기 위함
    P.insert(0, 0)
    DFS(1, 0)
    print(res)