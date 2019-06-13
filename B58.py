    
a,b=input().split()
a=int(a)
b=int(b)
c=0
temp=list(map(int,input().split()))
for x in temp:
    if(x==b):
        c=c+1
        break
if(c!=0):
    print("yes")
else:print("no")
