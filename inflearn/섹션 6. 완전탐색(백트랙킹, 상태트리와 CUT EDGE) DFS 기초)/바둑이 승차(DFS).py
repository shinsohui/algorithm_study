# ▣ 입력설명
# 첫 번째 줄에 자연수 C(1<=C<=100,000,000)와 N(1<=N<=30)이 주어집니다.
# 둘째 줄부터 N마리 바둑이의 무게가 주어진다.
#
# ▣ 출력설명
# 첫 번째 줄에 가장 무거운 무게를 출력한다.
#
# ▣ 입력예제 1
# 259 5
# 81
# 58
# 42
# 33
# 61
#
# ▣ 출력예제 1
# 242

from collections import deque

def DFS(L, sum, tsum):
    global result

    if sum + (total - tsum) < result:
        return

    if sum > c:
        return
    if L == n: # 부분 집합 하나 완성
        if sum > result:
            result = sum
    else:
        DFS(L+1, sum + a[L], tsum + a[L])
        DFS(L+1, sum, tsum + a[L])


if __name__ == "__main__":
    c, n = map(int, input().split())
    a = [0] * n
    result = -2147000000
    for i in range(n):
        a[i] = int(input())
    total = sum(a)
    DFS(0, 0, 0)
    print(result)
