
def getMinCores(start, end):
    MAX = 100000
    l=[]
    n=len(start)
    for i in range(n):
        l.append([start[i],end[i]])

    pre=[0]*MAX;

    for i in range(n) :
        pre[l[i][0]] += 1;
        pre[l[i][1] + 1] -= 1;
         
    ans = pre[0];
     
    for i in range(1, MAX) :
        pre[i] += pre[i - 1];
        ans = max(ans, pre[i]);
         
    return ans;

n=int(input())
start=list(map(int,input().split()))
n=int(input())
end=list(map(int,input().split()))

print(getMinCores(start, end))
