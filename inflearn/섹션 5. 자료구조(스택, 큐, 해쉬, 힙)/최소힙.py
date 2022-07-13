# ▣ 입력설명
# 첫 번째 줄부터 숫자가 입력된다. 입력되는 숫자는 100,000개 이하이며 각 숫자의 크기는 정 수형 범위에 있다.
#
# ▣ 출력설명
# 2) 연산을 한 결과를 보여준다.
#
# ▣ 입력예제 1
# 5
# 3
# 6
# 0
# 5
# 0
# 2
# 4
# 0
# -1
#
# ▣ 출력예제 1
# 3
# 5
# 2

import heapq as hq
a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)

