# ▣ 입력설명
# 첫째 줄에 자연수 N(1≤N≤1,000), M(1≤M≤N)이 주어진다. 다음 줄에는 조영필이 라이브에서 부른 순서대로 부른 곡의 길이가 분 단위로(자연수) 주어진다. 부른 곡의 길이는 10,000분을 넘지 않는다고 가정하자.
#
# ▣ 출력설명
# 첫 번째 줄부터 DVD의 최소 용량 크기를 출력하세요.
#
# ▣ 입력예제 1
# 9 3
# 1 2 3 4 5 6 7 8 9
#
# ▣ 출력예제 1
# 17

def Count(capacity):
    cnt = 1
    sum = 0
    for x in Music:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

n, m = map(int, input().split())
Music = list(map(int, input().split()))
# 최소한 노래 중 가장 긴 노래는 담을 수 있어야 한다.
maxx = max(Music)
lt = 1
rt = sum(Music)
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= maxx and Count(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)