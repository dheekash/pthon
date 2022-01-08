my_string = "Hello, World"

freq_dict = {}

for char in my_string.lower():
	if char.isalpha():
		if char in freq_dict:
			freq_dict[char] += 1
		else:
			freq_dict[char] = 1

print(freq_dict)
