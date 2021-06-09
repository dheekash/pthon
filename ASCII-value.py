def main(): # finding ASCII value of a given character 
   
    char = str(input("Plz enter the character to find it's ASCII value :"))
    print("The ASCII value is  : ", + ord(char)) #ord() function returns an integer representing the Unicode code point of the character

if __name__ == "__main__":
	main()
