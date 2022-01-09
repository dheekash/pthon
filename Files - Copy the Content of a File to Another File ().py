file1 = open('myfile.txt', 'r')
file2 = open('myfile2.txt', 'w')
l = []
l = file1.read()
print(l)
file2.writelines(l)
