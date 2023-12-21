n=int(input())
a=list(map(int,input().split()))
i=n-2
c=0
while i>=0:
    if a[i]>a[i+1] and a[i+1]==1 and a[i]-a[i+1]!=1:
        a=a[:i]+[a[i]-(a[i+1])]+[a[i+1]]+a[i+1:]
        c+=1
        i+=1
    elif a[i]>a[i+1]:
        a=a[:i]+[a[i]-(a[i+1]-1)]+[a[i+1]-1]+a[i+1:]
        c+=1
        i+=1
        
        
    #elif a[i]>a[i+1] and a[i]&1:
     #   a=a[:i]+[a[i]//2]+[(a[i]//2)+1]+a[i+1:]
      #  c+=1
       # i+=2
    i-=1
print(c,a)
