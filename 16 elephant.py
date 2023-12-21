l=[5,4,3,2,1]
x=int(input())
s=0
for i in l:
    q,r=divmod(x,i)
    s+=q
    x=r
print(s)
