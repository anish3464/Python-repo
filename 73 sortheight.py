import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
n=int(input())
l=list(map(int, input().split()))
n=int(input())
l2=list(map(int, input().split()))
print(sorted(l+l2))