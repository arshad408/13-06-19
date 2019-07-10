yx=int(input())
xs=2**yx
y=[]
for i in range(0,xs):
    l=bin(i)[2:].zfill(yx)
    if(len(l)<len(bin(2**yx-1)[2:])):
        y.append([l.count("1"),l])
    else:
        y.append([l.count("1"),l])
y.sort()
for i in range(len(y)):
    print(y[i][1])
