import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
n, k = map(int, input().split())
arr = sorted(set(map(int, input().split())))
final = arr[:k]
unq = set(final)
for i in range(0, n+1):
    if i not in unq:
        print(i)
        break