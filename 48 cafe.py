import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
from math import log2
def answer():
    no,k=map(int,input().split())
    l=[]
    for i in range(k):
        l.append(2**i)
    if log2(no)<k:
        ans=no+1
    else:
        ans=1<<k
    return ans

for _ in range(int(input())):
    print(answer())