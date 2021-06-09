def main(): # list basic actions  
    ar = []

    len = int(input("Enter the length of the list. "))

    for i in range(len):
        ar.append(int(input("Enter the elements :")))  #input

    for i in range(len):
        print(ar[i]) #output

    element = int(input("Enter the number to count from the list :"))
    print("The count of the element in the list is is : ", ar.count(element)) #count() method returns the number of times the specified element appears in the list

    ar.reverse() #Reverse a List
    print("\nReverse of List is :")
    for i in range(len):
        print(ar[i])

    ar.sort()
    print("\nSort of List is :")
    for i in range(len):
        print(ar[i])

if __name__ == "__main__":
	main()
