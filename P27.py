x,y=map(int,input().split())
z=list(map(int,input().split()))
v=list(map(int,input().split()))
t=[]
c=0
for i in range(x):
    x=v[i]/z[i]
    t.append(x)
while y>=0 and len(t)>0:
    mindex=t.index(max(t))
    if y>=z[mindex]:
        c=c+v[mindex]
        y=y-z[mindex]
    z.pop(mindex)
    v.pop(mindex
    t.pop(mindex)
print(c)
