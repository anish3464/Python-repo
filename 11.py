s=input()
a=[]
for i in s:
    if i not in a:
        a.append(i)
print("IGNORE HIM!" if len(a)&1 else "CHAT WITH HER!")
    
