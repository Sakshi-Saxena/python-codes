n = int(input())
li = [int(x) for x in input().split()]
rev_li = li[::-1]
if(rev_li == li):
    print("hannah will get treat!")
else:
    print("clay will get treat!")