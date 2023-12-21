import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w') 
tp,n=map(int,input().split())
p=[]
na=[]
tp11=tp
for i in range(n):    
    n1,p1=input().split()
    p.append(p1)
    na.append(n1)
for i in range(n):
    p[i]=int(p[i])
p2=p
p2.sort()
yes=[]
for i in range(n):
    if tp-p2[i]>0:
        tp-=p2[i]
        s=p.index(p2[i])
        yes.append(na[s])
    else:
        break
for i in na:
    if i in yes:
        print("I can afford",i)
    else:
        print("I can't afford",i)
if yes==[]:
    print("I need more Yen")
else:
    print(tp)
