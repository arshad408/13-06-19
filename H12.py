x,y=input().split()
z=input().split()
for i in range(int(b)):
    d=max(z,key=int)
    z.pop(z.index(max(z,key=int)))
print(d)
   
