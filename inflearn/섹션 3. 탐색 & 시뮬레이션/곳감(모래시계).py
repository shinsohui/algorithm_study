# ▣ 입력설명
# 첫 줄에 자연수 N(3<=N<=20) 이 주어며, N은 홀수입니다.
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
# 이 자연수는 각 격자안에 있는 감의 개수이며, 각 격자안의 감의 개수는 100을 넘지 않는다.
# 그 다음 줄에 회전명령의 개수인 M(1<=M<=10)이 주어지고, 그 다음 줄부터 M개의 회전명령 정보가 M줄에 걸쳐 주어집니다.

# ▣ 출력설명
# 총 감의 개수를 출력합니다.

# 입력 예제 1
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
# 3
# 2 0 3
# 5 1 2
# 3 1 4

# ▣ 출력예제 1
# 362

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0: # 왼쪽으로 밀 때
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0)) # 자동으로 왼쪽으로 당김
    else: # 오른쪽으로 밀 때
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop()) # 맨 뒤의 함수를 0번째 인덱스에 갖다놓기

# 모래시계 모양으로 더하기 
res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)


