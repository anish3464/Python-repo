import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
l=list(map(int,input().split()))
s=0
for i in range(64):
    if l[i]==1:
        s+=2**i
print(s)