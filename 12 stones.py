n=int(input())
s=input()
l=list(s[::])
c=0
i=0
while i<n-1:
    if l[i]==l[i+1]:
        del l[i+1]
        c+=1
        n-=1
        i=0
    else:
        i+=1
print(c)
    
