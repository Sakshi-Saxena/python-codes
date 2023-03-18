def isPossible(arr, n, m, mid):
    pageSum = 0
    studentCount = 1

    for i in range(n):
        if(arr[i] > mid):
            return False
        if(pageSum + arr[i] <= mid):
            pageSum += arr[i]
        else:
            studentCount += 1
            pageSum = arr[i]
            if(studentCount > m or arr[i] > mid):
                return False
        
        

    return True



def BookAllocation(arr, n, m):
    start = 0
    end = sum(arr)
    ans = -1
    # mid = start + (end - start)//2

    while(start <= end):
        mid = (start + end) // 2

        if(isPossible(arr, n, m, mid)):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

       
    
    return ans




arr = [10, 20, 30, 40]
n = len(arr) #no of books or len of arr
m = 2 #no of students
print(BookAllocation(arr, n, m))