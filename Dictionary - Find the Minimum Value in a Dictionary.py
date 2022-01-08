my_dict = {"a": 4, "b": 4, "c": 4, "d" : 5 , "e" : 6}
new_set = set(my_dict.values()) #converting values into set
print(new_set)
l = list(new_set)
l.sort()
print(l[0])

