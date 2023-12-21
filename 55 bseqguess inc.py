for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split())) 
    nl=[l[0]]
    i=1
    while l[i]!=l[m-1]:
        if l[i]<l[i-1]:
            
            i+=2
        else:
            nl.append(l[i])
            i+=1
        
