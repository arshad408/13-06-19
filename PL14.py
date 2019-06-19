    
a=int(input())
x=input()  
h=[]
x=list(x)  
for j in x:
      if(j=='A' or j=='E' or j=='I' or j=='O' or j=='U' or j=='a' or j=='e' or j=='i' or j=='o' or j=='u'):
          x.remove(j)
          h.append(j) 
I=x[ ::-1 ]
print(*I,sep=""); 
