import math

a =  int(input(print("Enter number : a")))
b =  int(input(print("Enter number : b")))
c =  int(input(print("Enter number : c")))

discriminant = b**2 - 4*a*c

if discriminant < 0:
	print("Complex Roots")
elif discriminant == 0:
	r = (-b + math.sqrt(discriminant))/(2*a)
	print(r)
else:
	r1 = (-b - math.sqrt(discriminant))/(2*a)
	r2 = (-b + math.sqrt(discriminant))/(2*a)
	print(r1, r2)
