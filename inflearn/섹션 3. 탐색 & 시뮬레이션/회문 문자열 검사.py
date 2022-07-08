# ▣ 입력설명
# 첫 줄에 정수 N(1<=N<=20)이 주어지고, 그 다음 줄부터 N개의 단어가 입력된다. 각 단어의 길이는 100을 넘지 않는다.
#
# ▣ 출력설명
# 각 줄에 해당 문자열의 결과를 YES 또는 NO로 출력한다.
#
# ▣ 입력예제 1
# 5
# level
# moon
# abcba
# soon
# gooG
#
# ▣ 출력예제 1
# #1 YES
# #2 NO
# #3 YES
# #4 NO #5 YES

n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size // 2):
        if s[j] != s[-1 - j]:
            print("#%d NO" % (i + 1))
            break
    else:
        print("#%d YES" % (i + 1))

#
# # Python 장점
# n = int(input())
# for i in range(n):
#     s = input()
#     s = s.upper()
#     if s == s[::-1]:
#         print("#%d YES" %(i+1))
#     else:
#         print("#%d NO" %(i+1))
