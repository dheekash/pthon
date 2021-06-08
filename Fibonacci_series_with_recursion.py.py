def fibo(num):

    if num <= 0:
        print("Incoreect input number  should  be more than 0 or equal to 0.")
    
    elif num == 1:
        print("The series is 1.")

    elif num == 2:
        print("The series is 1.")
    
    else:
        return(fibo(num-1) + fibo(num-2))   // error


def main(): # fibonacci series  
    
    num = int(input("Plz enter the nth  number to genrate fibbonaci numbers "))
    
    print("The Fibonacci series is : ")

    for i in range(num):
        print(fibo(i))

if __name__ == "__main__":
	main()
