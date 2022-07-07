# ▣ 입력설명
# 첫째 줄에 회의의 수 n(1<=n<=100,000)이 주어진다.
# 둘째 줄부터 n+1 줄까지 각 회의의 정 보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.
#
# ▣ 출력설명
# 첫째 줄에 최대 사용할 수 있는 회의 수를 출력하여라.
#
# ▣ 입력예제 1
# 5
# 1 4
# 2 3
# 3 5
# 4 6
# 5 7

# ▣ 출력예제 1
# 3
#
# 예제설명
# (2, 3) , (3, 5), (5, 7)이 회의실을 이용할 수 있다.

# 회의가 끝나는 시간으로 정렬
n = int(input())
meeting = []

for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

meeting.sort(key=lambda x: (x[1], x[0]))

et = 0
cnt = 0

for s, e in meeting:
    if s >= et: # 회의 끝 시간과 다음 시작 가능한 회의 시간 비교
        et = e
        cnt += 1
print(cnt)