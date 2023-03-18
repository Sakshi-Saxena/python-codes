# Python3 program to count
# number of subarrays having
# same minimum and maximum.

# calculate the no of contiguous
# subarrays which has same
# minimum and maximum
def calculate(a, n):
	
	# stores the answer
	ans = 0
	i = 0

	# loop to traverse from 0-n
	while(i < n):
		
		# start checking subarray
		# from next element
		r = i + 1

		# traverse for
		# finding subarrays
		for j in range(r, n):
			
			# if the elements are same
			# then we check further
			# and keep a count of same
			# numbers in 'r'
			if (a[i] == a[j]):
				r = r + 1
			else:
				break

		# the no of elements in
		# between r and i with
		# same elements.
		d = r - i

		# the no of subarrays that
		# can be formed between i and r
		ans = ans + (d * (d + 1) / 2)

		# again start checking
		# from the next index
		i = r - 1
		i = i + 1

	# returns answer
	return int(ans)

# Driver Code
a = [ 3, 3, 3, 1 ]
n = len(a)
print(calculate(a, n))

# This code is contributed by mits
