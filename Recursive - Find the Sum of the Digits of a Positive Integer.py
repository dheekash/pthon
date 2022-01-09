def sum(n):

    if n == 0:
      return 0
     
    if n > 0:
        
     return (n%10) + sum(n//10)
 
   
if __name__ == "__main__":
    n = int(input("Enter Number"))
    print(sum(n))
