import itertools

my_list = [1, 2, 3, 6]

permutations = list(itertools.permutations(my_list))

for permutation in permutations:
	print(permutation)
