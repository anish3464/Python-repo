from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from heapq import heapify, heappush, heappop
import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')


def solve():
    nM,nD=map(int, input().split())
    y,m,d=map(int, input().split())
    n=[]
    if d==nD:
        if m==nM:
            n=[y+1,1,1]
        else:
            n=[y,m+1,1]
    else:
        n=[y,m,d+1]
    print(*n)


solve()