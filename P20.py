
ax,ay=map(int,input().split())
mh=list(map(int,input().split()))
mh.sort()
mh.reverse()
ah=ay
z=0
for i in mh:
    if(ah>=i):
        no=int(ah/i)
        z=z+no
        ah=ah-no*i
    if ah==0:
        break
if(ah==0):
   print(z)
else:
   print("it's not posiible to select coins ",S)  
