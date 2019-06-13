a,b=map(int,input().split())
arr=list(map(int,input().split()))
arr2=list(map(int,input().split()))
flag = 0
if(all(x in arr for x in arr2)): 
    flag = 1
if(flag==0):
    print("NO")
else:
    print("YES")
