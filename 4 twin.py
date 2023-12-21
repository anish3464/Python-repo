n=int(input())
l=sorted(list(map(int,input().split())))
l=l[::-1]
s=0
for i in range(n):
    s+=l[i]
    s2=0
    for j in range(i+1,n):
        s2+=l[j]
    if s>s2:
        break
print(i+1)
