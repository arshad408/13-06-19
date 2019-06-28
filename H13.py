ar=list(input())
p=len(ar)
q=[]
r=[]
if p%2==0:
    for i in range(0,p//2):
        q.append(ar[i])
    for i in range(p//2,p):
        r.append(ar[i])
else:
    for i in range(0,p//2):
        q.append(ar[i])
    for i in range(p//2+1,p):
        r.append(ar[i])
q.sort()
r.sort()
if q==r:
    print('YES')
else:
    print('NO')
