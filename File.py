f1 = open("myfile.txt","r")
data = f1.read()
lines = data.split("\n")
#print(data)

for line in lines:
    words = line.split(" ")

    for word in words:
        print(word)
f1.close
