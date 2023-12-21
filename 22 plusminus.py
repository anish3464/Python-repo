for _ in range(int(input())):
    n=int(input())
    s=input()
    a=''
    for i in range(n-1):
        if s[i]=='0' or s[i+1]=='0':
            a+='+'
        else:
            a+='-'
    print(a)
    
