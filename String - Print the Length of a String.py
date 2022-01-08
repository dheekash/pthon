st = 'dheeraj'
i = input(print("Enter the index :"))
if len(st) == 0:
    print("Empty string")
elif int(i) < len(st):
    print(st[int(i)])
else:
    print("Index out of range"))
