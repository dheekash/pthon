def power(m,n):

    if n == 0:
      return 1
     
    elif n > 0:
        
     return m*power(m,n-1)
 
   
if __name__ == "__main__":
    m = int(input("Enter Number"))
    n = int(input("Enter the power"))
    print(power(m,n))
