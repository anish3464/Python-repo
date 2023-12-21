import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=0
for i in b:
    s+=a[i-1]
print(s)