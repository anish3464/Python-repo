import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
for _ in range(int(input())):
    l=list(map(int,input().split()))
    s=l[0]
    a,b=l[0],l[0]
    while(a>=0 and b>=0 and (l[1]>0 or l[2]>0)):
        while b>0 and l[1]>0:
            a+=1
            b-=1
            l[1]-=1
            s+=1
        while a>0 and l[2]>0 and b>=0:
            a-=1
            b+=1
            l[2]-=1
            s+=1
    while(l[3]>0 and a>=0 and b>=0):
        a-=1
        b-=1
        l[3]-=1
        s+=1
    print(s)
