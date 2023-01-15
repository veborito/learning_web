def move_zeros(lst):
	for el in lst:
		if el == 0:
			lst.pop(lst.index(el))
			lst.append(0)
	return lst

print('oh it worked yay !')