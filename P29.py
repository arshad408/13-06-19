def numb(x):
    m=0
    y=0
    l=[]
    while m<100 and m<x:
        c=0
        for x in str(x-m):
            c+=int(x)
        if c+(x-m)==x:
            y+=1
            l.append(x-m)
        m+=1
    print(y)  
    for m in l:
            print(m)
x=int(input())
numb(x)
