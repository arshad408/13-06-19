    
a=int(input())
b=list(map(int,input().split()))
for i in range(0,len(b)):
      if(b[i]%2==0 and i%2!=0):
              print(b[i],end=" ")
      elif(b[i]%2!=0 and i%2==0):
              print(b[i],end=" ")
