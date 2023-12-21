def summer(l):
    s=0
    for i in l:
        s+=i
    return s
n,d,p=map(int,input().split())
fare=sorted(list(map(int,input().split())),reverse=True)
tot_fare=0
pass_count=0
i=0
while i<n:
    if summer(fare[i:i+d])>p:
        tot_fare+=p
        i+=d
    else:
        break
tot_fare+=summer(fare[i:])

print(tot_fare)
    
    
    
    
