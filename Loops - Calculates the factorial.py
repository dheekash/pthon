num = int(input(print("Enter the number to calculate the factorial of :")))
fact = 1

for i in range(num):
    fact = fact + fact*i
    i = i+1
print(fact)

