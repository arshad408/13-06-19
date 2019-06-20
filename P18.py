p,r=map(int,input().split())
z=[]
x=0
for i in range(p):
    z.append(list(map(int,input().split())))   
for i in range(p):
    for j in range(r-1):
        for k in range(j+1,r+1):
            if z[i][j:k]==[1]*len(z[i][j:k]):
                 if all(z[p+i][j:k]==[1]*len(z[p+i][j:k]) for p in range(len(z[i][j:k])-1)):
                     if len(z[i][j:k])>x:
                        x=len(z[i][j:k])
if len(z)==1 and len(z[0])==1 and z[0][0]==1:
    print(1)
for i in range(x):
    print(*[1]*x) 
