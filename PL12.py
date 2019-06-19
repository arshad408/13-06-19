
p = list(map(int,input().split()))
q = list(map(int,input().split()))
for k in range(0,len(q)):
    print(q[(((len(q)-p[1])+k)%len(q))],end=' ')
