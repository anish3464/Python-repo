import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')

n = int(input())
l=list(map(int,input().split()))
a=[]
for i in range(n):
    n=l.index(i+1)
    a.append(n+1)
print(*[i for i in a])