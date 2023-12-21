import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
n=int(input())
s=input()
l=""
for i in s:
    l+=i
    l+=i
print(l)