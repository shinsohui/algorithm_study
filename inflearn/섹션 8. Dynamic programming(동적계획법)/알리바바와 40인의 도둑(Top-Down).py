# ▣ 입력설명
# 첫 번째 줄에는 자연수 N(1<=N<=20)이 주어진다.
# 두 번째 줄부터 계곡의 N*N 격자의 돌다리 높이(10보다 작은 자연수) 정보가 주어진다.
#
# ▣ 출력설명
# 첫 번째 줄에 (1, 1)출발지에서 (N, N)도착지로 가기 위한 최소 에너지를 출력한다.
#
# ▣ 입력예제 1
# 5
# 3 7 2 1 9
# 5 8 3 9 2
# 5 3 1 2 3
# 5 4 3 2 1
# 1 7 5 2 4
#
# ▣ 출력예제 1
# 25

def DFS(x, y):
    if dy[x][y] > 0:
        return dy[x][y] # 이미 계산한 값이 있다면 그 값을 사용

    if x == 0 and y == 0:
        return arr[0][0]
    else:
        if y == 0:
            dy[x][y] = DFS(x-1, y) + arr[x][y]
        elif x == 0:
            dy[x][y] = DFS(x, y-1) + arr[x][y]
        else:
            dy[x][y] = min(DFS(x-1, y), DFS(x, y-1)) + arr[x][y]

        return dy[x][y]

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)] # 메모이제이션
    print(DFS(n - 1, n - 1))