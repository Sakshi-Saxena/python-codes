def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fib(n):
    n1, n2 = 0, 1
    print(n1, n2, end=" ")
    for i in range(2, n):
        n3 = n1+n2
        n1= n2
        n2=n3
        print(n3, end=" ")
    print()

n = 10
fib(n)
for i in range(n):
    print(fibonacci(i), end=" ")