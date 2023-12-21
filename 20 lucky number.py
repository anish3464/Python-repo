s=input()
s=str(s)
l=list(s[::])
c=0
for i in l:
    if i=='4' or i=='7':
        c+=1
if c==4 or c==7:
    print("YES")
else:
    print("NO")
