import random # we need to import the library so that we can gerate a random password 
import datetime # using datetime module to calculate the current time

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # list of diffrent digits available 

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']                                       # list of diffrent lower case characters available
 
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']                                        # list of diffrent upper case characters available 
 
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']                                   # list of diffrent special characters available 
 
def password_genrator(password_num):                # function to generate the password
    rand_digit = random.choice(DIGITS)              # getting a random digit
    rand_upper = random.choice(UPCASE_CHARACTERS)   # getting a random upper case character
    rand_lower = random.choice(LOCASE_CHARACTERS)   # getting a random lower case character
    rand_symbol = random.choice(SYMBOLS)            # getting a random special case characters
    
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol # generating the passowrd by adding upp all the random characters we have produced so far using the choice function
    
    MAX_LENGTH = int(input("Plz enter the length of the password(minimum of 4 charcters will be generated). ")) # asking the user to enter the maximum lenght of the passowrd they need
    
    for i in range(MAX_LENGTH - 4): # loop to genrate the password
        temp_pass = temp_pass + random.choice(temp_pass)
   
    print("Your random Password is : " + temp_pass) #printing the password once it is genrated 
    
    return temp_pass # retunring the passowrd to the main program so the it can be strored in a file

def main(): # main function 

    next = 1 # initilazing next which we use to repeat the while loop and keep on genrating passwords
    
    password_num = 0 # number of the password genrated every time the program is executed

    ct = datetime.datetime.now() # ct stores current time   
    
    while next == 1:
            temp_pass = password_genrator(password_num) # calling the password genrator funtion
            password_num = password_num +1  
            next = int(input("Press 1 to continue generating passwords. "))
            file = open('password.txt','a') # appending the password file with the new password 
            file.write("Current time:- ")
            file.write(str(ct)) # writing the current time in file
            file.write(str(" || ")) 
            file.write("Password Number ")
            file.write(str(password_num)) 
            file.write(" :: ")  
            file.write(temp_pass)
            file.write("\n") # go the next line in file
            file.close()    #closing the flie once the new password is geratted  and stored in the file
            
if __name__ == "__main__":
	main()
