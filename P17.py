
x1,x2=input().split()  
x1=int(x1)  
x2=int(x2)   
v=list(map(int,input().split()))
count=0  
for i in range(len(v)):
  for j in range(i+1,len(v)):
    if (v[i]+v[j]==x2):
      count+=1
      break
if(count):
  print("yes")
else:
  print("no")
