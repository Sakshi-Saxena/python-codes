from math import factorial
# recurssion
def factRec(n):
    if n == 1:
        return 1
    
    return (n*factRec(n-1))

# loop
def factLoop(n):
    fact = 1
    for i in range(n, 0, -1):
        fact = fact*i
    return fact


n = int(input())
print(factorial(n))
print(factRec(n))
print(factLoop(n))




