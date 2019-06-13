x,y=map(int,input().split())
o=list(map(int,input().split()))
t=[]
for i in range(0,y):
    z=[]
    z=list(map(int,input().split()))
    q=f[0]
    for j in range(min(z)-1,max(z)):
        if q>o[j]: q=o[j]
    t.append(q)
for i in range(0,len(t)):
    print(t[i])
