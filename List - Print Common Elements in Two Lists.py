my_list1 = [1, 2, 3, 4]
my_list2 = [1, 2, 3]
my_list3 = []
for elem in my_list1:
	if elem  in my_list2:
		my_list3.append(elem)
print(my_list3)
