x=int(input())
list=list(map(int,input().split()))
for i in list:
    if list.count(i)>1:
        print(i)
        break
else:
    print("unique")
