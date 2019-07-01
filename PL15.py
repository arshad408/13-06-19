x1 = input()
x2y = []
for x in range(len(x1)):
  x2y.append(x1.count(x1[x]))
x = x2y.index(max(x2y))
print (x1[x])
