# ▣ 입력설명
# 첫째 줄에 자연수 N(3<=N<=100)이 주어집니다. 두 번째 줄에 N개로 구성된 수열이 주어집니다.
#
# ▣ 출력설명
# 첫째 줄에 최대 증가수열의 길이를 출력합니다.
# 두번째 줄에 가져간 순서대로 왼쪽 끝에서 가져갔으면 ‘L', 오른쪽 끝에서 가져갔으면 ’R'를 써간 문자열을 출력합니다.(단 마지막에 남은 값은 왼쪽 끝으로 생각합니다.)
#
# ▣ 입력예제 1
# 5
# 2 4 5 1 3
#
# ▣ 출력예제 1
# 4
# LRLL
#
# ▣ 입력예제 2
# 10
# 3 2 10 1 5 4 7 8 9 6
#
# ▣ 출력예제 2 3
# LRR

n = int(input())
a = list(map(int, input().split()))

lt = 0
rt = n-1
last = 0 # 처음 비교를 위함
res = ""

tmp = []

# 양 사이드에서 하나씩 가져와서 두개 비교하기
# 더 작은 수부터 배열에 추가한뒤 초기화하고 반복
# lt > rt 되면 종료
# 더 이상 tmp[-1]보다 큰 수 없으면 종료

while lt <= rt:
    # 우선 더 작은 수를 추가하기 위함
    if a[lt] > last:
        tmp.append((a[lt], 'L'))
    if a[rt] > last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break

    else:
        res = res+tmp[0][1]
        last = tmp[0][0]

        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear();

print(len(res))
print(res)


