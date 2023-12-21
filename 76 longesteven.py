from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from heapq import heapify, heappush, heappop
import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')


def solve():
    st=input()
    l=st.split()[::-1]
    d={}
    for i in l:
        if not len(i) & 1:
            d[len(i)]=i
            
    if len(d)==0:
        return "00"
    max=-1
    for i in d.keys():
        if i>max:
            max=i
            ms=d[i]
    return ms
    

for _ in range(int(input())):
    print(solve())