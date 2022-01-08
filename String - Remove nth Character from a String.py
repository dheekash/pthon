st = 'okiocwcm'
num = int(input(print("Enter the char index :")))

if  (len(st) == 0 ) or (num >= len(st)):
    print(st)


else:
    new_st = ""
    for i in range(len(st)):
        if i!=num:
            new_st = new_st + st[i]

    print(new_st)
