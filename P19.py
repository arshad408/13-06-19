p=int(input())
l1=[]
q=[]
for i in range(p):
    q=list(map(int,input().split()))
    for j in range(len(q)):
        l1.append(q[j])
l1.sort()
for i in range(len(l1)-1):
    print(l1[i],end=' ')
print(l1[len(l1)-1])
