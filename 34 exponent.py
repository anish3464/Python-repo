import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
for _ in range(int(input())):
    n = int(input())
    if n&1:
        print(-1)
    else:
        print(n//2,1)
    
