n = int(input("Enter the number : "))
mod = 0

while n > 0:
    mod = n %10
    print(int(mod))
    n = n//10
    
