def find_gcd(a, b):
	if b == 0:
		return a
	else:
		return find_gcd(b, a % b)



#num1 = int(input(print("Enter Number 1"))    
#num2 = int(input(print("Enter Number 2"))

print(find_gcd(5,10))
