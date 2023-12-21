n=int(input())
numbers=sorted(list(map(int,input().split())))
for i in range(n-1):
    if numbers[i+1]!=numbers[i]+1:
        print(numbers[i]+1)
        break
