def main(): # main function 
    num1 = 0
    num2 = 1
    num = int(input("Plz enter the nth  number to genrate fibbonaci numbers "))
    if num == 0:
        print("Incoreect input number  should  be more than 0 or equal to q.")
    elif num == 1:
        print("The series is 1.")
    else:   
        print("The Fibonacci series is : ")
        print(str(num1))
        print(str(num2))
        for i in range(2, num):
            num3 = num1 + num2
            num1 = num2
            num2 = num3
            print(str(num2))

if __name__ == "__main__":
	main()
