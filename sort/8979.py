N, K = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
li.sort(key=lambda x:(x[1],x[2],x[3]), reverse=True)
cnt = 1
if li[0][0] == K:
    print(1)
else:
    for i in range(1, N):
        if li[i][0] == K:
            print(cnt if li[i-1][1:] == li[i][1:] else i+1)
        if li[i-1][1:] != li[i][1:]:
            cnt = i+1