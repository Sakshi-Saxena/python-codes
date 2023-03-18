def isPossible(stalls, k, n, mid):
    cowCount = 1
    lastpos = stalls[0]
    
    for i in range(n):
        if(stalls[i] - lastpos >= mid):
            cowCount += 1
            if(cowCount == k):
                return True
            lastpos = stalls[i]
    return False      

def aggressiveCows(stalls, k):
    # Write your code here.
    n = len(stalls)
    stalls.sort()
    s = 0
    e = max(stalls)
    ans = -1
    while(s<=e):
        mid = (s+e)//2
        if(isPossible(stalls, k, n, mid)):
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
    return ans
            
stalls = [4, 2, 1, 3, 6]
k = 2
print(aggressiveCows(stalls, k))