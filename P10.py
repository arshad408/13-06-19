p=int(input())
q=[int(i) for i in input().split()]
x=0
for i in range(p):
	for j in range(i):
		if q[j]<q[i]:
			x+=q[j]
print(x)
