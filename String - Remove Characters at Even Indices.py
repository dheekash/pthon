st = "dheeraj kashyap"
new_st = ""

for i in range(len(st)):
    if i % 2 != 0:
        new_st = new_st + st[i]

print(new_st)
