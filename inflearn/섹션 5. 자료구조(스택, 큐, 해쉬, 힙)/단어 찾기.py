# ▣ 입력설명
# 첫 번째 줄에 자연수 N(3<=N<=100)이 주어진다.
# 두 번째 줄부터 노트에 미리 적어놓은 N개의 단어가 주어지고, 이어 바로 다음 줄부터 시에 쓰인 N-1개의 단어가 주어진다.
#
# ▣ 출력설명
# 첫 번째 줄에 시에 쓰지 않은 한 개의 단어를 출력한다.
#
# ▣ 입력예제 1
# 5
# big
# good
# sky
# blue
# mouse
# sky
# good
# mouse
# big

# ▣ 출력예제 1
# blue

# 딕셔러니 사용
n = int(input())
p = dict()

for i in range(n):
    word = input()
    p[word] = 1

for i in range(n - 1):
    word = input()
    p[word] = 0

for key, value in p.items():
    if value == 1:
        print(key)
        break

