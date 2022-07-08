# 입력예제
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 행과 열의 합 먼저 구하기
largest = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]  # 각 행마다의 합
        sum2 += a[j][i]  # 각 열마다의 합

    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

# 대각선의 합 구하기
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n - i - 1]

    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

print(largest)