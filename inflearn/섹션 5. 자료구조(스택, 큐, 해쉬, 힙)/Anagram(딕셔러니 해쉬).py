# ▣ 입력설명
# 첫 줄에 첫 번째 단어가 입력되고, 두 번째 줄에 두 번째 단어가 입력됩니다.
# 단어의 길이는 100을 넘지 않습니다.
#
# ▣ 출력설명
# 두 단어가 아나그램이면 “YES"를 출력하고, 아니면 ”NO"를 출력합니다.
#
# ▣ 입력예제 1
# AbaAeCe
# baeeACA
#
# ▣ 출력예제 1
# YES

a = input()
b = input()
str1 = dict()
str2 = dict()

for x in a:
    str1[x] = str1.get(x, 0) + 1

for x in b:
    str2[x] = str2.get(x, 0) + 1

print(str1, str2)

for i in str1.keys():
    if i in str2.keys():  # 우선 str1에 있는 값이 str2에도 있는지 확인
        if str1[i] != str2[i]:  # 있지만 count가 다르면 아나그램이 아님
            print("NO")
            break
    else:  # str1에 있는 값이 str2에 있지도 않은 경우
        print("NO")  # 아나그램이 아님
        break

else:  # 모든 필터를 통과하면 아나그램
    print("YES")
