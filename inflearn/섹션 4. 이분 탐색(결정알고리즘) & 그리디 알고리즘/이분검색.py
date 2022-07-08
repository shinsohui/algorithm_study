# ▣ 입력설명
# 첫 줄에 한 줄에 자연수 N(3<=N<=1,000,000)과 M이 주어집니다. 두 번째 줄에 N개의 수가 공백을 사이에 두고 주어집니다.
#
# ▣ 출력설명
# 첫 줄에 정렬 후 M의 값의 위치 번호를 출력한다.
#
# ▣ 입력예제 1
# 8 32
# 23 87 65 12 57 32 99 81
#
# ▣ 출력예제 1
# 3

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt = 0
rt = n-1

while lt <= rt:
    mid = (lt + rt)//2
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt = mid-1
    else:
        lt = mid+1


