from collections import Counter
s = input()
s2 = input()
# O(nlogn)
if(sorted(s) == sorted(s2)):
    print("anagram!")
else:
    print("not anagram!")

# O(n)
if(Counter(s) == Counter(s2)):
    print("anagram!")
else:
    print("not anagram!")