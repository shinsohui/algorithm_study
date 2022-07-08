n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:  # 더 이상 더할 수 없을 때
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1 # 좌측 포인터 이동
    else:
        tot -= a[lt]
        lt += 1 # 좌측 포인터 이동

print(cnt)