import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
for _ in range(int(input())):
    n = int(input())
    l=sorted(list(map(int,input().split())))
    if 0 in l:
        print("-1")
    else:
        for i in l:
            if i>0:
                print(i-1)
                break