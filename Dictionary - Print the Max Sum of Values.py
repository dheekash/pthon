my_dict = {
	"a": [1, 2, 3],
	"b": [4, 0, -4],
	"c": [3, 5, 9],
	"d": [45, 12, 100]
}

max_sum = None

for list_value in my_dict.values():
	list_sum = sum(list_value)

	if max_sum is None:
		max_sum = list_sum
	elif max_sum < list_sum:
		max_sum = list_sum

print(max_sum)
