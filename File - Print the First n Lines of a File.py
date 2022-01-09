f1 = open("myfile.txt","r")
n = int(input(print("Enter the number of lines to be printed")))
for i in range(n):
    print(f1.readline())
