import math
def prime(n):
    flag = False
    if n>1:
        for i in range(2, int(math.sqrt(n))+1):
            if(n%i == 0):
                flag = True
                break

        if(flag):
            return "Not prime!"
        else:
            return "prime No!"
    else:
        return "Not prime!"

n = int(input())
print(prime(n))

