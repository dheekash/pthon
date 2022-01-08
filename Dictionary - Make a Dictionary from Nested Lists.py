my_list = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]

new_dict = {}

for nested_list in my_list:
	key = nested_list[0] 
	value = nested_list[1]
	new_dict[key] = value

print(new_dict)
