
ar = int(input())
tr = int(ar/2)
ra = []
for i in range(ar, tr, -1):
    j = str(i)
    if i + sum([int(ka) for ka in j]) == ar:
        print(1)
        print(i)
        break
else:
    print(0) 
