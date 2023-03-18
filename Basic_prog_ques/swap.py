a = int(input())
b = int(input())
print("before swapping:", a, b)
a, b = b, a
print("after swapping:", a,b)

# using 3rd var
temp = a
a = b
b = temp
print("after swapping by using third var: ",a, b)

# without third var
a=a+b
b=a-b
a=a-b
print("after swapping without using third var: ",a, b)

