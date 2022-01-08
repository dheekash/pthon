st = "The quick brown fox jumps over the lazy dog"
new_st = ""

for i in range(len(st)):
    if st[i] != " ":
        new_st = new_st + st[i]
print(new_st)
