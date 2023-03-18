# Let sum of subset 1 be s1 and subset 2 with s2
# s1 - s2 = diff (given)
# s1 + s2=sum of array (logical)
# Therefore adding both eq we get :
# 2s1= diff + sum of array
# s1= (diff + sum of array)/2;
# Problem reduces to find no of subsets with given sum**

def countSubsetOfGivenDiff(arr, diff):
    n = len(arr)
    s = (sum(arr) + diff) // 2
    K = [[0] * (s+1) for x in range(n+1)]

    for i in range(n+1):
        for j in range(s+1):
            if i==0:
                K[i][j] = False
            if j == 0:
                K[i][j] = True
    
    for i in range(1, n+1):
        for j in range(s+1):
            if arr[i-1]<=j:
                K[i][j] = K[i-1][j-arr[i-1]] + K[i-1][j]
            else:
                K[i][j] = K[i-1][j]

    return K[n][s]


arr = [1, 1, 2, 3]
diff = 1
print(countSubsetOfGivenDiff(arr, diff))