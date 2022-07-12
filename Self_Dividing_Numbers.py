def sd(n):
    t = n
    while n>0:
        r = n%10
        if r == 0 or t%r != 0:
            return False
        n = n//10
    return True
l = int(input())
m = int(input())
for l in range(l,m+1):
    if sd(l) == True:
        print(l, end=' ')