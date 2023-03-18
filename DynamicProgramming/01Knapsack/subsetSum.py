def subsetSum(arr, n, sum):
    K = [[False for x in range(sum+1)]  for x in range(n+1)]
    #initialization
    for i in range(n+1):
        for j in range(sum+1):
            if(i==0):
                K[i][j] = False
            if(j==0):
                K[i][j] = True

    for i in range(1,n+1):
        for j in range(sum+1):
 
            if(arr[i-1] <= j):
                K[i][j] = (K[i-1][j-arr[i-1]] or K[i-1][j])
            if(arr[i-1] > j):
                K[i][j] = K[i-1][j]
    return K[n][sum]

arr = [2, 3, 7, 8, 10]
n = len(arr)
sum = 11
print(subsetSum(arr, n, sum))