def binary(n):
        #if n == 1:
            #print("1")
        #elif n == 0:
           # print("0")
         if n >= 1:    
            binary(n // 2)
            print(n % 2, end = '')
binary(21)
