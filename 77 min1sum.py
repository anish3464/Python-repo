
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from heapq import heapify, heappush, heappop
import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')


def solve(arr):
    l=1
    def ok(x):
        for elem in arr:
            if x + elem < 1:
                return 0
            x += elem
        return 1
    while (l <= r):
        mid = (l + r)//2
        if (ok(mid)):
            r = mid - 1
        else:
            l = mid +1
    return l
    
for _ in range(int(input())):
    arr=list(map(int, input().split()))
    print(solve(arr))