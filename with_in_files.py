"""f1= open("myfile.txt","w")
data=f1.write("help")
print(data)
f1.close()

---------------------using WITH---------------"""

with open("myfile.txt") as f1:
    data = f1.read()
    print(data)
