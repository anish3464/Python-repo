for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(l.sort())
    if l.sort()==l:
        print(n)
        print(*l)
        
