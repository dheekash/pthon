st = "The quick brow6n fox jumps over the lazy dog"
count = 0

ch = input("Enter the character to be counted : ")

for i in range(len(st)):
    if st[i] == ch:
        count = count + 1
        i = i + 1
    else :
        i = i + 1
print(count)        
        
