s=input()
f=list(s[:])
u,l=0,0
for i in f:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
if l>=u:
    print(s.lower())
else:
    print(s.upper())
