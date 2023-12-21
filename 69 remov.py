from collections import Counter
n,k=map(int,input().split())
l=list(map(int,input().split()))
d=Counter(l)
d=dict(sorted(d.items(), key=lambda item: item[1]))
for i in range(len(d)):
    if d[i]>=k:
        d[i]-=k
        k-=d[i]
    else:
        break
c=0
for i in d:
    if d[i]>0:
        c+=1
print(c)
        
    
