def isPrime(n): 
	if (n <= 1): 
		return False
	for i in range(2, n): 
		if (n % i == 0): 
			return False

	return True
if isPrime(int(input())): 
	print ("yes") 
else: 
	print ("no") 
	 


