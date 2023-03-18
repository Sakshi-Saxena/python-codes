import sympy
n = int(input())
print(sympy.isprime(n))
print(list(sympy.primerange(0, n)))
print(list(sympy.sieve.primerange(0, n)))