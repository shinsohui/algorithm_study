def draw(n, idx):
    if n == 1:
        starMap[idx][idx] = '*'
        return

    l = 4 * n - 3

    for i in range(idx, l + idx):
        # 위 아래
        starMap[idx][i] = '*'
        starMap[idx + l - 1][i] = '*'

        # 양 옆
        starMap[i][idx] = '*'
        starMap[i][idx + l - 1] = '*'

    return draw(n - 1, idx + 2)


n = int(input())
max_box = 4 * n - 3

starMap = [[' '] * max_box for _ in range(max_box)]

draw(n, 0)

for i in range(max_box):
    for j in range(max_box):
        print(starMap[i][j], end="")
    print()
