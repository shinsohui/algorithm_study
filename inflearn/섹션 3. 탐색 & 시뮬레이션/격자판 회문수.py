#  입력설명
# 1부터 9까지의 자연수로 채워진 7*7격자판이 주어집니다.

# ▣ 출력설명
# 5자리 회문수의 개수를 출력합니다.

# ▣ 입력예제 1
# 2 4 1 5 3 2 6
# 3 5 1 8 7 1 7
# 8 3 2 7 1 3 8
# 6 1 2 3 2 1 1
# 1 3 1 3 5 3 2
# 1 1 2 5 6 5 2
# 1 2 2 2 2 1 5

# ▣ 출력예제 1
# 3

board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):  # 어차피 5자리임
    for j in range(7):
        tmp = board[j][i:i + 5]
        if tmp == tmp[::-1]:
            cnt += 1

        # 열에서 회문 검사
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt += 1

print(cnt)