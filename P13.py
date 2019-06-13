x,r=map(int,input().split())
p=list(map(int,input().split()))
z=[]
for i in range(0,r):
    x=[]
    x=list(map(int,input().split()))
    q=f[0]
    for j in range(min(x)-1,max(x)):
        if q>p[j]: q=p[j]
    z.append(q)
for i in range(0,len(z)):
    print(z[i])
