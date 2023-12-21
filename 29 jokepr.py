import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
s=input()
l="HQ9"
f=0
for i in l:
    if i in s:
        print("YES")
        f=1
        break
if not f:
    print("NO")
