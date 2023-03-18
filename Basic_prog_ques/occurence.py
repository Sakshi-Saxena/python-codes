s= input()
search = input()
c=0
for i in s:
    if i == search:
        c+=1
print(c)
print(s.count(search))