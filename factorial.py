def factorial(num):
    if num < 0:
        return 0
    elif num == 0 or num == 1:
        return 1
    else:
        fact = 1
        while(num > 1):
            fact *= num
            num -= 1
        return fact

def main():
    num = int(input("Enter the number to perform  the factorial. ")) 
    fact = factorial(num)
    print("The Factorial is " + str(fact) )
if __name__ == "__main__":
	main()
