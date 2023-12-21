import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
for _ in range(int(input())):
    n=int(input())
    s = input()
    ns=""
    d=""
    i=0
    while i<n-1:
        for j in range(i+1,n):
            if s[i]==s[j] :
                ns+=s[i]
                i=j
                break
        i+=1
    print(ns)