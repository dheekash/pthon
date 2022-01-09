def binary_search(seq, low, high, elem):
	if low > high:
		return -1
	else:
		middle = (low + high)//2

		if elem == seq[middle]:
			return middle
		elif elem < seq[middle]:
			return binary_search(seq, low, middle-1, elem)
		else:
			return binary_search(seq, middle+1, high, elem)
