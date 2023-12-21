import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
def searchMatrix(matrix, target):
        l=0
        r=len(matrix)-1
        while l<=r:
            m=(l+r)//2
            if matrix[m][0]<=target:
                l=m+1
            else:
                r=m-1
        l=0
        d=r
        r=len(matrix[r])-1
        while l<=r:
            m=(l+r)//2
            if matrix[d][m]<=target:
                l=m+1
            else:
                r=m-1
        return target==matrix[d][r]
