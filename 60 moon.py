n,m,p=map(int,input().split())
c=0
for i in range(n):
    if m+(i*p)>n:
        break
    else:
        c+=1
print(c)
