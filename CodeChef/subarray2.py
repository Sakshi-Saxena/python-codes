# cook your dish here
def sub_lists (l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists
 
# driver code
t = int(input())
count = 0
for i in range(t):
    n, k = map(int, input().split())
    l = [int(x) for x in input().split()]
    if(max(sub_lists(l)) == min(sub_lists(l))):
        count = count + 1 
    print(count)