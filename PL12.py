
p,q=map(int,input().split())
o=list(map(int,input().split()))
for i in range(q):
  for l in range(p-1,0,-1):
    O[l],O[l-1]=O[l-1],O[l]
print(*O)
