s=input()
l=[]
for i in s:
    if i in "123":
        l.append(int(i))
s=""
l.sort()
for i in range(len(l)):
    s+=str(l[i])
    if i!=len(l)-1:
        s+="+"
print(s)
