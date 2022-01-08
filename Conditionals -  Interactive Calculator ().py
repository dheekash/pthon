ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4
INTEGER_DIVISION = 5
MODULO = 6

print("=== Welcome to your Interactive Python Calculator ===")

a = int(input("Please enter the first value: "))
b = int(input("Please enter the second value: "))

print("Great! Now enter the operation.")
print("These are the available options:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Integer Division")
print("6 - Modulo")

operation = int(input("--> Enter the corresponding integer: "))

if operation == ADDITION:
	result = a + b
	print(f"The result of {a} + {b} is: {result}")
elif operation == SUBTRACTION:
	result = a - b
	print(f"The result of {a} - {b} is: {result}")
elif operation == MULTIPLICATION:
	result = a * b
	print(f"The result of {a} * {b} is: {result}")
elif operation == DIVISION:
	if b == 0:
		print("Division by Zero. Please enter another value for b.")
	else:
		result = a / b
		print(f"The result of {a} / {b} is: {result}")
elif operation == INTEGER_DIVISION:
	if b == 0:
		print("Division by Zero. Please enter another value for b.")
	else:
		result = a // b
		print(f"The result of {a} // {b} is: {result}")
elif operation == MODULO:
	result = a % b
	print(f"The result of {a} % {b} is: {result}")
else:
	print("Please choose a valid operation.")
