n=int(input())
arr=list(map(int,input().split()))
s=0
for i in range(n):
    cn=arr[i+2:].count(arr[i])
    if cn==1:
        k=arr.index(arr[i],i+2,n)
        s+=(k-i)-1
    elif cn>1:
        pyind= [index for (index, item) in enumerate(arr) if item == arr[i]]
        for k in pyind[1:]:
            s+=(k-i)-1
        
print(s)
