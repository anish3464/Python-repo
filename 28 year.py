import sys, os
if os.environ.get('DEBUG'):
    sys.stdin=open('inputs.txt', 'r')
    sys.stdout=open('outputs.txt','w')
def check(n):
    n += 1
    if len(set(str(n)))==len(str(n)):
        return n
    return check(n)
print(check(int(input())))

