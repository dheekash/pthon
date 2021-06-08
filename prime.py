def main():
    num = int(input("Enter the number to perform the check if it's a prime no. ")) 
    
    if num > 1:

        for i in range(2, int(num/2)+1): # the loop needs to run only  num/2+1 times to check for prime
 
             if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    
    else:
        print(num, "is not a prime number")

if __name__ == "__main__":
	main()
