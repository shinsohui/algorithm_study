# ▣ 입력설명
# 첫 번째 줄에 자연수 N(1<=N<=10)이 주어집니다.
# 두 번째 줄에 집합의 원소 N개가 주어진다. 각 원소는 중복되지 않는다.
#
# ▣ 출력설명
# 첫 번째 줄에 “YES" 또는 ”NO"를 출력한다.
#
# ▣ 입력예제 1
# 6
# 1 3 5 6 7 10
#
# ▣ 출력예제 1
# YES
import sys


def DFS(L, sum):
    if sum > total // 2:
        return

    if L == 6:
        if sum == (total - sum):
            print("YES")
            sys.exit(0)

    else:
        DFS(L + 1, sum + a[L]) # 원소를 사용하겠다. a[L]값 증가
        DFS(L + 1, sum) # 원소를 사용하지 않겠다.


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")
