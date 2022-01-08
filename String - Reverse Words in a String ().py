st = "The quick brown fox jumps over the lazy dog"
new_st = ""
num = len(st)
num = num - 1

while num >= 0:
    new_st = new_st + st[num]
    num = num - 1 

print(new_st)
