from math import gcd
for _ in range(int(input())):
    left,right=map(int,input().split())
    if left==1 and right==3:
        print(-1)
    elif left==1 and right==2:
        print(-1)
    elif left==2 and right==3:
        print(-1)
    else:
        print(right//2,right//2)