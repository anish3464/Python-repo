n=int(input())
l=[]
for i in range(n):
    temp=list(map(int,input().split()))
    l.append(temp)
    l=sorted(l,key=lambda x: x[2],reverse=True)
temp=0
for i in range(n):
    while l[i][0]<=l[i][1]:
        l[i][0]+=1
        l[i][1]-=1
        temp+=1
print(temp)
