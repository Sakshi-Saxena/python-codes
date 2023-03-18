mod=int(1e9+7)

sz=int(2e5+5);fac=[1]*sz;

for i in range(1,sz):
    fac[i]=fac[i-1]*i%mod
    
for _ in range(int(input())):
    n=int(input())
    
    d={};dic={};
    l=[int(x) for x in input().split()]
    
    for i in l:
        d.setdefault(i,0)
        d[i]+=1
    
    for i in d:
        c=d[i]
        
        for j in range(1,c+1):
            dic.setdefault((c-j)-(j-1),0)
            dic[(c-j)-(j-1)]+=1 
            
    res=1
    for i in dic:
        res=res*fac[dic[i]]%mod
        
    print(res)