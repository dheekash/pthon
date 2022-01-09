n = int(input("Enter the number : "))

if n==0 or n == 1:
    print("Not Prime")

else:
    for i in range(2,n):
        if n%i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
