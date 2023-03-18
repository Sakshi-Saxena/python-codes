#count of subset sum of given sum
def SubsetSumCount(arr, sum, n):
    K = [[0] * (sum + 1) for i in range(n + 1)]
    
    #initialization
    for i in range(n+1):
        for j in range(sum+1):
            if(i==0):
                K[i][j] = 0
            if(j==0):
                K[i][j] = 1

    for i in range(1,n+1):
        for j in range(1, sum+1):
 
            if(arr[i-1] <= j):
                K[i][j] = (K[i-1][j-arr[i-1]] + K[i-1][j])
            else:
                K[i][j] = K[i-1][j]
    return K[n][sum]


arr = [2, 3, 5, 6, 8, 10]
n = len(arr)
sum = 10
print(SubsetSumCount(arr, sum, n))