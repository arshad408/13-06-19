x= int(input())
a= list(map(int,input().split()))
for i in range(0,x-2):
  for j in range(i+1,x-1):
    for k in range(j+1,x):
      if a[i]+a[j] == a[k]:
        print(a[i],a[j],a[k])
