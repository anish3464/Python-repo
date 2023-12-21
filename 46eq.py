for _ in range(int(input())):
    x=int(input())
    for i in range(1,x):
        for j in range(1,x):
            for k in range(1,x):
                if i*j+k==x:
                    print(i,j,k)
