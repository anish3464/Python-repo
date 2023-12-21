import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
for _ in range(int(input())):
    n = int(input())
    l=list(map(int,input().split()))
    ce,co=0,0
    for i in l:
        if i & 1:
            co+=i
        else:
            ce+=i
    if co>=ce:
        print("NO")
    else:
        print("YES")
     