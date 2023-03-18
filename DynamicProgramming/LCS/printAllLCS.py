N = 100
dp = [[0 for i in range(N)]
		for j in range(N)]
def findLCS(x, y, m, n):
	s = set()

	if m == 0 or n == 0:
		s.add("")
		return s

	if x[m - 1] == y[n - 1]:
		tmp = findLCS(x, y, m - 1, n - 1)
		for string in tmp:
			s.add(string + x[m - 1])


	else:
		if dp[m - 1][n] >= dp[m][n - 1]:
			s = findLCS(x, y, m - 1, n)
		if dp[m][n - 1] >= dp[m - 1][n]:
			tmp = findLCS(x, y, m, n - 1)		
			for i in tmp:
				s.add(i)
	return s


def LCS(x, y, m, n):
	for i in range(m + 1):
		for j in range(n + 1):
			if i == 0 or j == 0:
				dp[i][j] = 0
			elif x[i - 1] == y[j - 1]:
				dp[i][j] = dp[i - 1][j - 1] + 1
			else:
				dp[i][j] = max(dp[i - 1][j],
							dp[i][j - 1])
	return dp[m][n]

# Driver Code

x = "AGTGATG"
y = "GTTAG"
m = len(x)
n = len(y)
print("LCS length is", LCS(x, y, m, n))

s = findLCS(x, y, m, n)

for i in s:
	print(i)


