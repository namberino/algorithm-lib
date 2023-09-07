def count_partitions(n):
    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
    dp[0][0] = 1

    # Iterate through each possibilities
    for i in range(1, n + 1):
        for j in range(n + 1):
            if j >= i:
                dp[i][j] = dp[i - 1][j] + dp[i][j - i]
            else:
                dp[i][j] = dp[i - 1][j]
                
    return dp[n][n]


n = 5
print(count_partitions(n))
