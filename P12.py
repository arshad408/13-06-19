ax,bx=map(int,input().split())
o=list(map(int,input().split()))
x=[]
for i in range(0,bx):
    b=[]
    b=list(map(int,input().split()))
    v=0
    for j in range(min(b)-1,max(b)):
        v=v+o[j]
    x.append(v)
for i in range(0,len(x)):
    print(x[i])
