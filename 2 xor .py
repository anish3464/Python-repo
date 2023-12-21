for _ in range(int(input())):
    n=int(input())
    l=[]
    if n%2!=0:
        for i in range(n):
            l.append(n)
    else:
        for i in range(n-2):
            l.append(2)
        l.append(1)
        l.append(3)
    print(*[x for x in l])
        
