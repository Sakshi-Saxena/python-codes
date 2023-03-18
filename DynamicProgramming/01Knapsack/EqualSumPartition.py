def EqualSumPartition(arr, s, n):
    #sum of array
    arr_sum = sum(arr)
    if(arr_sum % 2 != 0):
        return False
    else:
        sum_ = arr_sum//2
        K = [[False for x in range(sum_+1)] for x in range(n+1)]
        for i in range(n+1):
            for j in range(sum_+1):
                if(i==0):
                    K[i][j] = False
                if(j==0):
                    K[i][j] = True

        for i in range(n+1):
            for j in range(sum_+1):
 
                if(arr[i-1] <= j):
                    K[i][j] = (K[i-1][j-arr[i-1]] or K[i-1][j])
                if(arr[i-1] > j):
                    K[i][j] = K[i-1][j]
    return K[n][sum_]


arr = [1, 5, 11, 5]
n = len(arr)
s = 22
print(EqualSumPartition(arr, s, n))