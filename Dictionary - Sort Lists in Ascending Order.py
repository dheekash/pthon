my_dict = {
	"a": [4, 3, 2],
	"b": [5, 3, 7],
	"c": [1, 9, 10],
	"d": [3, 4, 1]
}

for list_value in my_dict.values():
	list_value.sort()

print(my_dict)
