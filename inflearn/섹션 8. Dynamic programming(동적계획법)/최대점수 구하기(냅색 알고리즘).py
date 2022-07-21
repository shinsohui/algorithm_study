# ▣ 입력설명
# 첫 번째 줄에 문제의 개수N(1<=N<=100)과 제한 시간 M(10<=M<=1000)이 주어집니다.
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

if __name__ == "__main__":
    n, m = map(int, input().split())
    dy = [0] * (m + 1)
    for i in range(n):
        ps, pt = map(int, input().split())
        for j in range(m, pt-1, -1):
            dy[j] = max(dy[j], dy[j - pt] + ps)

    print(dy[m])

