a=int(input())
b=list(map(int,input().split()))
l=max(b)
e,f=0,0
for i in range(0,len(b)):
  for j in range(i+1,len(b)):
    if abs(b[i]+b[j])<l:
      e,f=b[i],b[j]
      l=abs(e+f)
print(e,f)
