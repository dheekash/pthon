f1 = open("myfile.txt","r")
longest = ""
for word in f1:
    if len(word) > len(longest):
        longest = word
print(longest)
    
    
