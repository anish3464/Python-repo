k,n,w=map(int,input().split())
i=1
p=0
while i<=w:
    p+=(k*i)
    i+=1
print(p-n if p>n else "0")
