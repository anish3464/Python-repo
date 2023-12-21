import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')

n = int(input())
l=list(map(int,input().split()))
a=[]
s=1
i=0
m=0
while i<n:
    for j in range(i,n-1):
        if l[j]<=l[j+1]:
            s+=1
        else:
            break
    if s>m:
        m=s
    s=1
    i=j
print(m)