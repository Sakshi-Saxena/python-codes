def LongestCommonSubstring(x, y, m, n):
    res = 0
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if(i==0 or j==0):
                dp[i][j] = 0

    for i in range(m+1):
        for j in range(n+1):
            if(x[i-1] == y[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
                res = max(res, dp[i][j])
            else:
                dp[i][j] = 0
    
    return res


x = "abcdgh"
y = "abedfhr"
n = len(y)
m = len(x)
print(LongestCommonSubstring(x, y, m, n))