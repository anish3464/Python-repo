import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
for _ in range(int(input())):
    n = int(input())
    l=sorted(list(map(int,input().split())))
    if n==1:
        print(1)
    else:    
        o=l.count(1)
        n-=o
        a=(o+1)//2
        a+=n
        print(a)