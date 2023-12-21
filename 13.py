def check():
    for _ in range(int(input())):
        n=int(input())
        a=input()
        b=input()
        a=list(a[::])
        b=list(b[::])
        s=a
        l=[1,2,3,5,7,11,13,17,19,23,29]
        f=0
        for i in range(len(a)):
            if a==b:
                print("YES")
                f=1
                return
            for k in l:
                while k<len(a):
                    for j in range(i,k):    
                        if s[j]=='1':
                            s[j]='0'
                        else:
                            s[j]='1'
                if s==b:
                    print("YES")
                    f=1
                    return
        if f!=1:
            print("NO")
            return 
        else:
            print("YES")
            return
check()
