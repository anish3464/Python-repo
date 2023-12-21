import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')

def min_sum_product(arr1, arr2, n, k):
    diff = 0
    SUM = 0
    temp = 0
    for i in range(n):
        pro = arr1[i] * arr2[i]
        SUM += pro
        if pro < 0 and arr2[i] < 0:
            temp = (arr1[i] + 2 * k) * arr2[i]
        elif pro < 0 and arr1[i] < 0:
            temp = (arr1[i] + 2 * k) * arr2[i]
        elif pro > 0 and arr2[i] < 0:
            temp = (arr1[i] - 2 * k) * arr2[i]
        elif pro > 0 and arr1[i] > 0:
            temp = (arr1[i] - 2 * k) * arr2[i]
        d = abs(pro - temp)
        if d > diff:
            diff = d
    return SUM - diff

n, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = min_sum_product(arr1, arr2, n, k)
print(result)