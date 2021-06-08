def main(): # fibonacci series using array 
    array = [0,1] #initilazin the first 2 digits
    
    num = int(input("Plz enter the nth  number to genrate fibbonaci numbers "))
    
    if num <= 0:
        print("Incoreect input number  should  be more than 0 or equal to 0.")
    
    elif num == 1:
        print("The series is 1.")
    
    else:   
        for i in range (2, num):
            array.append(array[i-1] + array[i-2])

        print("The Fibonacci series is : ")
    for i in range(0,num):
        print(str(array[i]))
        i += 1
  
if __name__ == "__main__":
	main()
