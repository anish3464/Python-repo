s=0
m=-1
for _ in range(int(input())):
    a,b=map(int,input().split())
    s-=a
    s+=b
    if s>m:
        m=s
print(m)
    
