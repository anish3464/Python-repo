import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
from math import sqrt
# def ifthere(n):
#     l=1
#     r=18
#     while l<r:
#         mid=l+r//2
#         if n==mid**mid:
#             return mid
#         elif n<mid**mid:
#             r=mid-1
#         else:
#             l=mid+1
#     return -1
# n=int(input())
# print(ifthere(n))


def ifthere(n):
    l = -1
    r = 18

    def ok(x):
        return (x ** x) <= n
    while l <= r:

        mid = (l + r)//2

        if (ok(mid)):
            l = mid + 1
        else:
            r = mid - 1
    if (r**r) == n:
        print(r)
    else:
        print(-1)


n = int(input())
ifthere(n)

