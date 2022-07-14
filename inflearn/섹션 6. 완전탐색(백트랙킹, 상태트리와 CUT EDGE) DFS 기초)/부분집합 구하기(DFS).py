# ▣ 입력설명
# 첫 번째 줄에 자연수 N(1<=N<=10)이 주어집니다.
#
# ▣ 출력설명
# 첫 번째 줄부터 각 줄에 하나씩 부분집합을 아래와 출력예제와 같은 순서로 출력한다. 단 공집합은 출력하지 않습니다.
#
# ▣ 입력예제 1
# 3
#
# ▣ 출력예제 1
# 1 2 3
# 1 2
# 1 3
# 1
# 2 3
# 2
# 3

def DFS(v):
    if v == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v] = 1
        DFS(v + 1)
        ch[v] = 0
        DFS(v+1)


if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n+1)
    DFS(1)