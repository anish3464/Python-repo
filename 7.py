a=[]
for _ in range(5):
    l=list(map(int,input().split()))
    a.append(l)
s=0
for i in range(5):
    for j in range(5):
        if a[i][j]==1:
            s+=abs((i+1)-3)+abs((j+1)-3)
print(s)
