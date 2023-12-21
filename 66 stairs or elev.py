x,y=map(int,input().split())
if x<y:
    n=y-x<=2
else:
    n=x-y<=3
if n:
    print("Yes")
else:
    print("No")
