def LCS_Recurssive(x, y, m, n):
    if(m==0 or n==0):
        return 0
    
    if(x[m-1] == y[n-1]):
        return 1 + LCS_Recurssive(x, y, m-1, n-1)
    else:
        return max(LCS_Recurssive(x,y,m-1,n), LCS_Recurssive(x,y,m,n-1)) 

def LCS_Memoization(x, y, m, n):
    if(m == 0 or n == 0):
        return 0
    
    dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]

    if(dp[m][n] != -1):
        return dp[m][n]

    elif(x[m-1] == y[n-1]):
        dp[m][n] = 1 + LCS_Memoization(x, y, m-1, n-1)
        return dp[m][n]
    else:
        dp[m][n] = max(LCS_Memoization(x, y, m-1, n), LCS_Memoization(x, y, m, n-1))
        return dp[m][n]


def LCS_topDown(x, y, m, n):
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if(i==0 or j==0):
                dp[i][j] = 0

    for i in range(m+1):
        for j in range(n+1):
            if(x[i-1] == y[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]


x = "abcdgh"
y = "abedfhr"
n = len(y)
m = len(x)
print(LCS_Recurssive(x, y, m, n))
print(LCS_Memoization(x, y, m, n))
print(LCS_topDown(x, y, m, n))