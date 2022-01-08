my_dict = {"a": 1, "b": 2, "c": 3}
key = input(print("Enter KEY"))
value = input(print("Enter Value"))

if key not in my_dict:
    my_dict[key] = value
else:
    print("Key Present ")
print(my_dict)

