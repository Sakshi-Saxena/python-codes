# How do you get the matching elements in an integer array?

arr = [int(x) for x in input().split()]
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i] == arr[j]):
            print(arr[i])
