import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
n,k=map(int,input().split())
s=input()
t=list("x"*n)
pas=0
for i in range(n):
    if pas<k:
        if s[i]=='o':
            t[i]='o'
            pas+=1
    else:
        break
for i in t:
    print(i,end="")
