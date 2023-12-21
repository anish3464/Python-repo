n,health,bar=map(int,input().split())
potions=list(map(int,input().split()))
ans=0
for i in range(n):
    if potions[i]+health>=bar:
        ans=i+1
        break
print(ans)
