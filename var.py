n=input()
x=0
y=0
for i in n:
    if i.isalpha()==True:
        x=1
    elif i.isdigit()==True:
        y=1
if (x==1 and y==1):
    print("Yes")
else:
    print("No")
