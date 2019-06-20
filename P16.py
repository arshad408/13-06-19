
p=int(input())
q=list(map(int,input().split()))
x=[1]*p
for i in range(p):
    if i==0:
        if q[i]>q[i+1]:
            x[i]=x[i]+x[i+1]
    elif i>0:
        if q[i]>q[i-1]:
            x[i]=x[i]+x[i-1]
print(sum(x))
