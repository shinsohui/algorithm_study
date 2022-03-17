from sys import stdin

input = stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
result = 0


def dfs(i, graph, total):
    global result, s, n
    if total == s:
        result += 1

    # graph (부분수열) 만들기
    for j in range(i + 1, n):
        dfs(j, graph, total + graph[j])


for i in range(0, n):
    dfs(i, nums, nums[i])

print(result)