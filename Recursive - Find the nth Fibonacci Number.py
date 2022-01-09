def fib(n):
    if n <= 1:
      return n
     
    if n > 0:
     return fib(n-1) + fib(n-2)
 
   
if __name__ == "__main__":
    print(fib(9))
