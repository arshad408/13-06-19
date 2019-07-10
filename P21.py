x=int(input())
y=list(map(int,input().split()))
e=int(x/2)
h=y[:e]
sh=y[e::]
if ((sum(h)//len(h))==(sum(sh)//len(sh))):
    print("yes")
else:
    print("no")
