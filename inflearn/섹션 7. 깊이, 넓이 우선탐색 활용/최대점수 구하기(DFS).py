# ▣ 입력설명
# 첫 번째 줄에 문제의 개수N(1<=N<=20)과 제한 시간 M(10<=M<=300)이 주어집니다.
# 두 번째 줄부터 N줄에 걸쳐 문제를 풀었을 때의 점수와 푸는데 걸리는 시간이 주어집니다.
#
# ▣ 출력설명
# 첫 번째 줄에 제한 시간안에 얻을 수 있는 최대 점수를 출력합니다.
#
# ▣ 입력예제 1
# 5 20
# 10 5
# 25 12
# 15 8
# 6 3
# 7 4
#
# ▣ 출력예제 1
# 41

def DFS(L, sum, time):
    # print(L, sum, time)
    global res

    if time > m:
        return

    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L + 1, sum + pv[L], time + pt[L])
        DFS(L + 1, sum, time) # 안풀고 넘어감


if __name__ == "__main__":
    n, m = map(int, input().split())
    pv = list() # 점수
    pt = list() # 푸는 시간

    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)

    res = -2147000000
    DFS(0, 0, 0)
    print(res)