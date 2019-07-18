
p=input()
for i in range(1,len(p)):
    if ord(p[i])>ord(p[0]):
        ansr=p[i:]
        break
print(ansr)
