import heapq

n,q=input().split(" ")

n=int(n)

q=int(q)

an=list(map(int,input().split(" ")))

s=sum(an)

ax=an.copy()

ax=[i*-1 for i in ax]

heapq.heapify(an)

heapq.heapify(ax)

l=[]

for i in range(q):

    c=int(input())

    l.append(c)

    z=[0]*n

    z[0]=s

for i in range(1,n):

    t1=heapq.heappop(ax)

    t1=-1*t1

    t2=heapq.heappop(an)

    s=(s-(t1+t2)+(t1-t2))

    z[i]=s

    heapq.heappush(an,(t1-t2))

    heapq.heappush(ax,-1*(t1-t2))

for i in l:

    print(z[i])

#  gdb or hackerearth spcl array operation