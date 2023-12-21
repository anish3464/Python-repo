
import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')

from math import ceil
def solve():
    n,m,a=map(int, input().split())
    print(ceil(n/a)*ceil(m/a))
solve()

