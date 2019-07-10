ay=int(input())
ys=list(map(int,input().split()))[:ay]
s=sum(ys[0:ay:2])
y=sum(ys[1:ay:2])
if s>y:
  print(s)
else:
  print(y)
