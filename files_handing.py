"""filename="myflie.txt"
fileobj=open(filename,"w")


fileobj.write("BASH\n")

fileobj.close()

"""

filename = "myfile.txt"
fileobj = (filename,"r")
for line in fileobj:
    print(line)
#fileobj.close()



