n = int(input())
dp = [0 for _ in range(90)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, n):
    for j in range(i-1): # i자릿수 - 2 까지 전부 더하고 +1
        dp[i] += dp[j]
    dp[i] += 1
print(dp[n-1])