st = 'dheeraj kashyap'
leng = len(st)
num = leng - 3
if leng < 6:
    print("empty string")
else:
    print(st[1])
    leng = leng - 1 

    while num <= leng:
        print(st[leng])
        leng = leng - 1 
