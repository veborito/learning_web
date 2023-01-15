def move_zeros(lst):
	for el in lst:
		if el == 0:
			lst.pop(lst.index(el))
			lst.append(0)
	return lst

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))œ