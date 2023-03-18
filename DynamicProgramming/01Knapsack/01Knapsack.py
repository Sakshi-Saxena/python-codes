def Knapsack(wt, val, W, n):
    K = [[-1 for x in range(W+1)] for x in range(n+1)]

    #base condition
    if n==0 or W==0:
        return 0
    #memoization
    if K[n][W] != -1:
        return K[n][W]
    
    #choice diagram code
    if wt[n-1] <= W:
        K[n][W] = max(val[n-1] + Knapsack(wt, val, W-wt[n-1], n-1), Knapsack(wt, val, W, n-1))
        return K[n][W]

    elif wt[n-1] > W:
        K[n][W] =  Knapsack(wt, val, W, n-1)
        return K[n][W]



def TopDownKnapsack(wt, val, W, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for n in range(n+1):
        for w in range(W+1):
            if(n==0 or w==0):
                K[n][w] = 0

            if(wt[n-1] <= w):
                K[n][w] = max(val[n-1] + K[n-1][w-wt[n-1]], K[n-1][w])
              
            elif(wt[n-1] > w):
                K[n][w] =  K[n-1][w]
                
    return K[n][W]

wt = [10, 20, 30]
val = [60, 100, 120]
W = 50
n = len(val)
print(TopDownKnapsack(wt, val, W, n))