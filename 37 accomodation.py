import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')

n = int(input())
s=0
for i in range(n):
    p,q=map(int,input().split())
    if q-2>=p:
        s+=1
print(s)