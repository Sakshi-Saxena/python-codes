import sys

def minSubsetSumDiff(arr, n):
    sum_ = sum(arr)
    K = [[False for x in range(sum_+1)]  for x in range(n+1)]
    #initialization
    for i in range(n+1):
        for j in range(sum_+1):
            if(i==0):
                K[i][j] = False
            if(j==0):
                K[i][j] = True

    for i in range(1,n+1):
        for j in range(sum_+1):
 
            if(arr[i-1] <= j):
                K[i][j] = (K[i-1][j-arr[i-1]] or K[i-1][j])
            if(arr[i-1] > j):
                K[i][j] = K[i-1][j]
    
    #minsubsetsumdiff
    diff = sys.maxsize

    for j in range(sum_//2, -1, -1):
        if K[n][j] == True:
            diff  = sum_ - (2 * j)
            break
    
    return diff

arr = [1, 6, 11, 5]
n = len(arr)
print(minSubsetSumDiff(arr, n))