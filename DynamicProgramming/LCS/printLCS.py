def printLCS(x, y, m, n):
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
    
    lcs = " "
    i = m
    j = n
    while(i>0 or j>0):

        if(x[i-1] == y[j-1]):
            lcs += x[i-1]
            i -= 1
            j -= 1

        else:
            if(dp[i-1][j] > dp[i][j-1]):
                i -= 1

            else:
                j-=1

    lcs = lcs[::-1]
    return lcs

x = "acbcf"
y = "abcdaf"
m = len(x)
n = len(y)
print(printLCS(x,y,m,n))