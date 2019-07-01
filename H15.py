
rx=int(input())
x=list(map(int,input().split()))
c=0
p=[]
q=[]
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if x[i]<x[j]:
            c=c+1
            break
    else:
        p.append(x[i])        
print(*p)
print(max(x))
