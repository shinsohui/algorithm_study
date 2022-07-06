# ▣ 입력설명
# 첫 번째 줄에 완성된 9×9 스도쿠가 주어집니다.
#
# ▣ 출력설명
# 첫째 줄에 “YES" 또는 ”NO"를 출력하세요.

# ▣ 입력예제 1
# 1 4 3 6 2 8 5 7 9
# 5 7 2 1 3 9 4 6 8
# 9 8 6 7 5 4 2 3 1
# 3 9 1 5 4 2 7 8 6
# 4 6 8 9 1 7 3 5 2
# 7 2 5 8 6 3 9 1 4
# 2 3 7 4 8 1 6 9 5
# 6 1 9 2 7 5 8 4 3
# 8 5 4 3 9 6 1 2 7
#
# ▣ 출력예제 1
# YES

def check(a):
    for i in range(9):
        ch1 = [0] * 10 # 행 체크를 위함
        ch2 = [0] * 10 # 열 체크를 위함
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False # 둘 중 하나라도 만족하지 않으면 스도쿠 X
    # 그룹 체크
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            # 그룹 안에서 숫자 체크
            for k in range(3):
                for s in range(3):
                    ch3[a[i * 3 + k][j * 3 + s]] = 1
            if sum(ch3) != 9:
                return False
    return True


a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")
