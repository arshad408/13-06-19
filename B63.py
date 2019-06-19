a=input()

flag=True

for i in a:

  if i!='0' and i!='1':

    flag=False

    break

if flag==False:

  print("no")

else:

  print("yes")
