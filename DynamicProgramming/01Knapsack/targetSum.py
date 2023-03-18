# similar as Count no of subset of given diff but asked differently 
# Given an array of integers A[] of length N and an integer target.
# You want to build an expression out of A by adding one of the symbols '+' and '-' before each integer
#  in A and then concatenate all the integers.

def TargetSum(arr, target):
    N = len(arr)
    s1, c = 0, 0
    for i in range(N):
        if(arr[i] == 0):
            c+=1
        s1+=arr[i]  

    if((target+s1)%2 != 0):
        return 0

    if(target == s1):
        return 2**c
        
    else:
        s = (s1 + target) // 2
        K = [[0]*(s+1) for x in range(N+1)]

        for i in range(N+1):
            for j in range(s+1):
                if i==0:
                    K[i][j] = 0
                if j == 0:
                    K[i][j] = 1 
        for i in range(1, N+1):
            for j in range(1, s+1):
                if arr[i-1]<=j:
                    K[i][j] = K[i-1][j-arr[i-1]] + K[i-1][j]
                else:
                    K[i][j] = K[i-1][j]
    
    return K[N][s]




arr = [9, 2, 9]
sORdiff = 3
print(TargetSum(arr, sORdiff))