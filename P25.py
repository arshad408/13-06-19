n=int(input())
l=input().split()
nl=[]
for i in range(n):
    s=l[i]
    for j in range(i+1,n):
        if(int(l[i])<int(l[j]))and (int(l[j-1])<int(l[j])):
            s+=l[j]
        else:
            break
    nl.append(len(s))
print(max(nl))
