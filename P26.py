
def lis(arra): 
    x = len(arra) 
    lis = [1]*x 
    for i in range (1 , x): 
        for j in range(0 , i): 
            if arra[i] > arra[j] and lis[i]< lis[j] + 1 : 
                lis[i] = lis[j]+1
    maximum = 0
    for i in range(x): 
        maximum = max(maximum , lis[i])  
    return maximum 
a=int(input()) 
arra = list(map(int,input().split()))
print (lis(arra))
