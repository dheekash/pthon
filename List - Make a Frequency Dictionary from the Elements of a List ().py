my_list = ["a", "a", "b", "c", "a", "b"]

freq_dict = {}

for elem in my_list:
	if elem not in freq_dict:
		freq_dict[elem] = 1
	else:
		freq_dict[elem] += 1

print(freq_dict)
