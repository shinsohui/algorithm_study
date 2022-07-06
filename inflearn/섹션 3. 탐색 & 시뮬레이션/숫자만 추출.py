# ▣ 입력설명
# 첫 줄에 숫자가 썩인 문자열이 주어집니다. 문자열의 길이는 50을 넘지 않습니다.
#
# ▣ 출력설명
# 첫 줄에 자연수를 출력하고, 두 번째 줄에 약수의 개수를 출력합니다.
#
# ▣ 입력예제 1
# g0en2Ts8eSoft
#
# ▣ 출력예제 1
# 28
# 6

s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)

print(res)
cnt = 0
for i in range(1, res + 1):
    if res % i == 0:
        cnt += 1

print(cnt)
