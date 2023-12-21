import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
def fact(n):
    f=1
    while n>0:
        f*=n
        n-=1
    return f
for _ in range(int(input())):
    n = int(input())
    s=fact(n)
    