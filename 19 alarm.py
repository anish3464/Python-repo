def jigi(a,b,c,d):
    s=b
    l=b
    if b<a and d>c:
        return -1
    while s<a:
        s+=c-d
        l+=c if c>d else d
    return l
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    print(jigi(a,b,c,d))
