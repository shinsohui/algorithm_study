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
# 1 2
# 1 3
# 2 1
# 2 3
# 3 1
# 3 2
# 6
# 중복 순열에서 중복을 허용하지 않으면 된다.
# 사용 유무를 체크하는 배열을 하나 생성

def DFS(L):
    global cnt

    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1

    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L + 1)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    ch = [0] * (n + 1)
    DFS(0)
    print(cnt)

