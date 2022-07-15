# ▣ 입력설명
# 첫 번째 줄에 숫자로 암호화된 코드가 입력된다. (코드는 0으로 시작하지는 않는다, 코드의 길이는 최대 50이다) 0이 입력되면 입력종료를 의미한다.
#
# ▣ 출력설명
# 입력된 코드를 알파벳으로 복원하는데 몇 가지의 방법이 있는지 각 경우를 출력한다. 그 가지수도 출력한다. 단어의 출력은 사전순으로 출력한다.
#
# ▣ 입력예제 1
# 25114
#
# ▣ 출력예제 1
# BEAAD
# BEAN
# BEKD
# YAAD
# YAN
# YKD
# 6

def DFS(L, P):
    global cnt
    if L == n:
        cnt += 1
        for j in range(P):
            print(chr(res[j] + 64), end='')
        print()

    else:
        for i in range(1, 27):
            if code[L] == i:
                res[P] = i
                DFS(L + 1, P + 1)

            elif i >= 10 and code[L] == i//10 and code[L + 1] == i%10: # -1에 의해 절대 거
                res[P] = i
                DFS(L + 2, P + 1)


if __name__ == "__main__":
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1) # n번째에 -1 추가함
    res = [0] * (n+3)
    cnt = 0
    DFS(0, 0)
    print(cnt)
