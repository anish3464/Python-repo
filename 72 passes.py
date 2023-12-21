
import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')


for _ in range(int(input())):
    n,curr=map(int, input().split())
    for i in range(n):
        r=input().split()
        c=r[0]
        if c=='P':
            prev=curr
            curr=r[1]
        else:
            temp=curr
            curr=prev
            prev=temp
    print("Player",curr)

