
a=int(input())
li=list(map(int,input().split()))
li.sort()
x=0
y=0
for i in range(len(li)):
    if li[i]>=x:
        y=y+1
    x=x+li[i]
print(y)
