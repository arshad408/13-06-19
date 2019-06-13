a=int(input())
b=list(map(int,input().split()))
l=max(b)
d,f=0,0
for i in range(0,len(b)):
  for j in range(i+1,len(b)):
    if abs(b[i]+y[j])<l:
      d,f=b[i],b[j]
      l=abs(d+f)
print(d,f)
