from itertools import permutations
n=input()
a=permutations(n)
for j in list(a):
    print("".join(j))
