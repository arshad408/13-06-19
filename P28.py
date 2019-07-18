ar=int(input())
br=[int(s) for s in input().split()]
br.sort()
s=0
xv=0
for i in range(len(br)):
    if br[i]>=s:
        xv+=1
    s=s+br[i]
print(xv)
