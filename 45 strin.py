import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
for _ in range(int(input())):
    n = int(input())
    s = input()
    flag=1
    for i in set(s):
        cond = 1
        p=3
        for pos,ele in enumerate(s, start=1):
            if ele == i:
                if p ==3:
                    p = pos&1
                    continue
                if pos&1!=p:
                    flag=0
    print("YES" if flag==1 else "NO")