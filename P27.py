
AA,BB=map(int,input().split())
CC=list(map(int,input().split()))
pr=list(map(int,input().split()))
qr=[]
ar=0
for i in range(AA):
    x=pr[i]/CC[i]
    qr.append(x)
while BB>=0 and len(qr)>0:
    mindex=qr.index(max(qr))
    if BB>=CC[mindex]:
        ar=ar+pr[mindex]
        BB=BB-CC[mindex]
    CC.pop(mindex)
    pr.pop(mindex)
    qr.pop(mindex)
print(ar)
