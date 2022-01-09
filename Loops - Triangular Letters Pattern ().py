n = int(input("Enter the number : "))
char = 65
for row in range(1, n+1):
    for col in range(1,row+1):
        print(chr(char), end = " ")
    print()
    char = char + 1

