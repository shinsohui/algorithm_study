# ▣ 입력설명
# 첫 줄에 자연수 N이 주어진다.(1<=N<=50)
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는다.
#
# ▣ 출력설명
# 봉우리의 개수를 출력하세요.
#
# ▣ 입력예제 1
# 5
# 5 3 7 2 3
# 3 7 1 6 1
# 7 2 5 3 4
# 4 3 6 4 1
# 8 7 3 5 2
#
# ▣ 출력예제 1
# 10

# 상 우 하 좌 (시계방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.insert(0, [0] * n)
a.append([0] * n)

# 각 행마다 맨 앞, 맨 뒤에 0을 추가
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)