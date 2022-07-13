# ▣ 입력설명
# 첫째 줄에 숫자(길이는 1000을 넘지 않습니다)와 제가해야할 자릿수의 개수가 주어집니다.
#
# ▣ 출력설명
# 가장 큰 수를 출력합니다.
#
# ▣ 입력예제 1
# 5276823 3
#
# ▣ 출력예제 1
# 7823
#
# ▣ 입력예제 2
# 9977252641 5
#
# ▣ 출력예제 2
# 99776

# pop() 할 수 있는 수가 0이 될 때까지
# 숫자의 앞에 더 큰 숫자가 있으면 pop()하고 앞으로 전진

num, m = map(int, input().split())
num = list(map(int, str(num)))

stack = []
for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

# 남은 m 처리
if m != 0:
    stack = stack[:-m]

res = ''.join(map(str, stack))
print(res)

