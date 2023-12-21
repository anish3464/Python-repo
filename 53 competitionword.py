for _ in range(int(input())):
    l=[]
    for i in range(int(input())):
        a,b=map(int,input().split())
        if a>10:
            l.append(0)
        else:
            l.append(b)
    print(l.index(max(l))+1)
