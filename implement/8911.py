import sys

input = sys.stdin.readline

t = int(input())


def fr():
    k[0] = min(now[0], k[0])
    k[1] = min(now[1], k[1])
    k[2] = max(now[0], k[2])
    k[3] = max(now[1], k[3])


def go(m):
    for i in range(2):
        now[i] += p[m][i]
    fr()


while t:
    t -= 1
    k = [0, 0, 0, 0]  # minX, minY, maxX, maxY
    s = list(input())
    now = [0, 0]
    d = 0
    p = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for i in s:
        if i == "F":
            go(d)
        if i == "B":
            go((d + 2) % 4)
        if i == "L":
            d -= 1
            d %= 4
        if i == "R":
            d += 1
            d %= 4
    # print(k)
    print((k[2] - k[0]) * (k[3] - k[1]))