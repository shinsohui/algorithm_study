# ▣ 입력설명
# 첫줄에 정수의 개수 N(3<=N<=20)과 임의의 정수 K(2<=K<=N)가 주어지고,
# 두 번째 줄에는 N개의 정수가 주어진다.
# 세 번째 줄에 M이 주어집니다.
#
# ▣ 출력설명
# 총 가지수를 출력합니다.
#
# ▣ 입력예제 1
# 5 3
# 2 4 5 8 12
# 6
#
# ▣ 출력예제 1
# 2

# 내 풀이
# def DFS(L, s):
#     global cnt
#     total = 0
#     if L == k:
#         for j in range(L):
#             # print(res[j], end=' ')
#             total += res[j]
#         # print("total =", total)
#         if total % m == 0:
#             cnt += 1
#
#     else:
#         for i in range(s, len(a) + 1):
#             res[L] = a[i - 1] # 조합으로
#             DFS(L + 1, i + 1)
#
#
# if __name__ == "__main__":
#     n, k = map(int, input().split())
#     a = list(map(int, input().split())) # a는
#     m = int(input())
#     res = [0] * len(a) # res에는
#     cnt = 0
#     DFS(0, 1)
#
#     print(cnt)
#
def DFS(L, s, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(L + 1, i + 1, sum + a[i])


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split())) # a는
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)