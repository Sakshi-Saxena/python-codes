s = input().split()
dict = {}
for i in s:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)