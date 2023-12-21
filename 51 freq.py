import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
n=int(input())
l=list(map(int,input().split()))
s1=[]
s2=[]
for i in range(3*n):
    if l[i] not in s1:
        s1.append(l[i])
    elif l[i] not in s2:
        s2.append(l[i])
    if len(s2)==n:
        break
print(*s2)