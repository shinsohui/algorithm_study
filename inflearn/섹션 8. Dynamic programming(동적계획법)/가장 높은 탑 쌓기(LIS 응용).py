# ▣ 입력설명
# 입력 파일의 첫째 줄에는 입력될 벽돌의 수가 주어진다. 입력으로 주어지는 벽돌의 수는 최대 100개이다. 둘째 줄부터는 각 줄에 한 개의 벽돌에 관한 정보인 벽돌 밑면의 넓이, 벽돌의 높 이 그리고 무게가 차례대로 양의 정수로 주어진다. 각 벽돌은 입력되는 순서대로 1부터연속적 인 번호를 가진다.
#
# ▣ 출력설명
# 첫 번째 줄에 가장 높이 쌓을 수 있는 탑의 높이를 출력한다.
#
# ▣ 입력예제 1
# 5
# 25 3 4
# 4 4 6
# 9 2 3
# 16 2 5
# 1 5 2
#
# ▣ 출력예제 1
# 10

if __name__ == "__main__":
    n = int(input())
    bricks = []

    for i in range(n):
        a, b, c = map(int, input().split())
        bricks.append((a, b, c)) # tuple 형태로
        bricks.sort(reverse=True) # 넓이를 기준으로 내림차순으로 소팅
        dy = [0] * n # dynamic list (높이 저장)
        dy[0] = bricks[0][1]
        res = bricks[0][1]

    for i in range(1, n): # i번째 벽돌은 내가 만들고자하는 벽돌탑의 가장 상단에 위치하는 벼돌
        max_h = 0
        for j in range(i-1, -1, -1):
            if bricks[j][2] > bricks[i][2] and dy[j] > max_h:
                max_h = dy[j]
        dy[i] = max_h + bricks[i][1]
        res = max(res, dy[i])
    print(res)
