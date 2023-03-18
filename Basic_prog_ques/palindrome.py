def palindrome(n):
    if(n == n[::-1]):
        return "palindrome!"
    else:
        return "not palindrome!"


def traditionalPalindrome(n):
    temp = n
    rev = 0
    while(n>0):
        dig = n%10
        rev = rev*10 + dig
        n=n//10
    if(temp == rev):
        return "palindrome!"
    else:
        return "not palindrome!"

n = input()
print(palindrome(n))
print(traditionalPalindrome(int(n)))



