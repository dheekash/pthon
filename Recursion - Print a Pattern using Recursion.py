def pattern(n):
        if n ==1:
                print("*")
        else:
                print("*"*n)
                pattern(n-1)
pattern(6)
