def isPossible(boards, k, mid, n):
    pageSum = 0
    stdCount = 1
    for i in range(n):
        if(boards[i] > mid):
            return False
        if(pageSum + boards[i] <= mid):
            pageSum += boards[i]
        else:
            stdCount += 1
            pageSum = boards[i]
            if(stdCount > k or boards[i] > mid):
                return False
    return True

def PainterPartition(boards, k):
    n = len(boards)
    s = 0
    e = sum(boards)
    ans = -1
    while(s <= e):
        mid = (s+e) // 2
        if(isPossible(boards, k, mid, n)):
            ans = mid
            e = mid - 1
        else:
            s = mid + 1
    return ans 

arr = [5,5,5,5]
k = 2
print(PainterPartition(arr, k))
