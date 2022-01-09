f1 = open("myfile.txt","r")
n = int(input(print("Enter the number of lines to be printed")))
lines = f1.readlines()
last_lines = lines[-n:]
print(last_lines, end= "")
