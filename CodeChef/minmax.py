
# def maximumSubarraySum(arr):
#        n = len(arr)
#        maxSum = -1e8
#        currSum = 0

#        for i in range(0, n):
#            currSum = currSum + arr[i]
#            if(currSum > maxSum):
#                maxSum = currSum
#            if(currSum < 0):
#                currSum = 0
      
#        return maxSum



def minimumSubarraySum(arr):
       n = len(arr)
       minSum = 1e9+7
       currSum = 0

       for i in range(0, n):
           currSum = currSum + arr[i]
           if(currSum < minSum):
               minSum = currSum
           if(currSum > 0):
               currSum = 0
      
       return minSum


def minSum(arr, n):
	
	sum = arr[0]; prev = arr[0]

	for i in range(1, n):

		# If violation happens, make current
		# value as 1 plus previous value and
		# add to sum.
		if arr[i] <= prev:
			prev = prev + 1
			sum = sum + prev

		# No violation.
		else :
			sum = sum + arr[i]
			prev = arr[i]

	return sum

# Drivers code
arr = [ 2, 2, 3, 5, 6 ]
n = len(arr)
print(minSum(arr, n))

# This code is contributed by Ansu Kumari


l = [1, 2, 3]
print(minimumSubarraySum(l))

# t = int(input())
# count = 0
# for i in range(t):
#     n, k = map(int, input().split())
#     l = [int(x) for x in input().split()]
#     if(maximumSubarraySum(l) == minimumSubarraySum(l)):
#         count += 1
#     print(count)