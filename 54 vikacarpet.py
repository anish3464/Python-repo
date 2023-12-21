for _ in range(int(input())):
    m,n=map(int,input().split())
    f=0
    l=[]
    for i in range(m):
        s=input()
        if set("vika").issubset(s):
            print("YES")
            f=1
            break
        l.append(s)
    if not f:
        for j in range(n):
            name=""
            for i in range(m):
                name+=l[i][j]
            if name=="vika":
                print("YES")
                f=1
                break
    if not f:
        print("NO")
