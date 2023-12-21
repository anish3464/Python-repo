n=int(input())
arr=list(map(int,input().split()))
s=0
for i in arr:
    m=0
    for j in str(i):
        if int(j)>m:
            m=int(j)
    s+=m        
print(s)
